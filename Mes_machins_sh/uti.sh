#!/bin/bash
# creer_users_sans_sudo.sh
# Usage: ./creer_users_sans_sudo.sh liste.txt
# Produit: utilisateurs.csv (nom;prenom;login;password) et ajouter_users_root.sh (script à exécuter en root)

set -euo pipefail
IFS=$'\n\t'

INPUT="${1:-}"
OUT="utilisateurs.csv"
ROOT_SCRIPT="ajouter_users_root.sh"

if [[ -z "$INPUT" || ! -f "$INPUT" ]]; then
  echo "Usage: $0 liste.txt" >&2
  exit 1
fi

# Choix de la commande pour générer un hash (utile pour useradd -p)
if command -v mkpasswd >/dev/null 2>&1; then
  hash_cmd(){ mkpasswd -m sha-512 "$1"; }
elif command -v openssl >/dev/null 2>&1; then
  hash_cmd(){ openssl passwd -6 "$1"; }
else
  # Si aucun outil pour hasher, on mettra une valeur vide dans le -p et l'admin devra forcer le mot de passe
  hash_cmd(){ echo ""; }
fi

umask 077
echo "nom;prenom;login;password" > "$OUT"

# Prépare le script à lancer en root (protégé)
echo "#!/bin/bash" > "$ROOT_SCRIPT"
echo "# Script généré automatiquement — exécuter en root (sudo) pour créer les comptes" >> "$ROOT_SCRIPT"
echo "" >> "$ROOT_SCRIPT"

chmod 700 "$ROOT_SCRIPT"

while IFS= read -r line || [[ -n "$line" ]]; do
  # ignorer lignes vides ou commençant par #
  [[ -z "${line//[[:space:]]/}" ]] && continue
  [[ "$line" =~ ^[[:space:]]*# ]] && continue

  prenom="${line%% *}"
  nom="${line#* }"

  # nettoyage très simple : minuscules, enlever espaces du nom
  prenom_lc="$(echo -n "$prenom" | tr '[:upper:]' '[:lower:]')"
  nom_lc="$(echo -n "$nom" | tr '[:upper:]' '[:lower:]' | tr -d ' ')"

  # login = initiale du prénom + nom
  base="$(echo -n "${prenom_lc:0:1}$nom_lc" | tr -cd 'a-z0-9')"
  login="$base"
  # On ne vérifie pas l'existence dans /etc/passwd (pas de sudo) — l'admin verra les collisions
  # Si tu souhaites garantir unicité locale, on peut ajouter un compteur basé sur OUT existant :
  i=1
  while grep -q -i "^.*;.*;${login};" "$OUT" 2>/dev/null; do
    login="${base}${i}"
    i=$((i+1))
  done

  # mot de passe aléatoire (10 chars)
  password="$(tr -dc 'A-Za-z0-9' </dev/urandom | head -c 10 || echo "Pass12345")"
  hash="$(hash_cmd "$password")"

  # Écrire ligne CSV
  echo "${nom};${prenom};${login};${password}" >> "$OUT"

  # Ajouter commande au script root : si hash vide, on utilisera useradd simple + chpasswd
  if [[ -n "$hash" ]]; then
    # Utiliser -p avec le hash (useradd attend un hash crypt)
    echo "useradd -m -s /bin/bash -c \"${prenom} ${nom}\" -p '${hash}' ${login} || echo 'Échec useradd ${login}'" >> "$ROOT_SCRIPT"
    echo "chage -d 0 ${login} || true" >> "$ROOT_SCRIPT"
  else
    # Si pas de hash généré, on ajoute useradd sans -p puis chpasswd (nécessite root)
    echo "useradd -m -s /bin/bash -c \"${prenom} ${nom}\" ${login} || echo 'Échec useradd ${login}'" >> "$ROOT_SCRIPT"
    # chpasswd attend "login:password" sur stdin ; on ajoute une ligne qui lira depuis EOF
    echo "echo '${login}:${password}' | chpasswd || echo 'Échec chpasswd ${login}'" >> "$ROOT_SCRIPT"
    echo "chage -d 0 ${login} || true" >> "$ROOT_SCRIPT"
  fi

  echo "Préparé: $login"
done < "$INPUT"

echo ""
echo "Fini."
echo "- Fichier contenant les comptes et mots de passe : $OUT"
echo "- Script à exécuter en root pour créer les comptes : $ROOT_SCRIPT"
echo ""
echo "Pour créer réellement les comptes :"
echo "  sudo bash $ROOT_SCRIPT"
echo ""
echo "PS: garde $OUT en lieu sûr et supprime-le après usage (ex: shred -u $OUT)."

