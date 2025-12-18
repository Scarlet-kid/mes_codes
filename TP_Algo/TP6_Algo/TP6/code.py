import os
def invert_pbm(filename):
    # Ouverture du fichier source
    with open(filename,"r") as f:
        magic = f.readline().strip()
        if magic != "P1":
            raise ValueError("seul le format PBM ASCII (P1) est géré")

        # On lit le reste
        tokens = f.read().split()
    width = int(tokens[0])
    height = int(tokens[1])
    pixels = tokens[2:]

    if len(pixels) != width*height:
        raise ValueError("Nombre de pixels incohérent avec les dimensions")

    # Inversion des pixels
    invert_pixels = []
    for p in pixels:
        if p=="0":
            invert_pixels.append("1")
        elif p=="1":
            invert_pixels.append("0")
        else:
            raise ValueError(f"pixel invalide : {p}")

    # Nom du fichier de sortie:
    root, ext = os.path.splitext(filename)
    outname = root + "Reverse" + ext

    # Ecriture du nouveau fichier
    with open(outname,"w") as out:
        out.write("P1\n")
        out.write(f"{width} {height}\n")
        for i,p in enumerate(invert_pixels):
            out.write(p)
            if(i+1) % width == 0:
                out.write("\n")
            else:
                out.write(" ")
    print(f"Image inversée écrite dans : {outname}")

if __name__ == "__main__":
    nom = input("Nom du fichier PBM:")
    try:
        invert_pbm(nom)
    except Exception as e:
        print("Erreur :",e)