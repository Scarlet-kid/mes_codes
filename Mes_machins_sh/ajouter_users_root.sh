#!/bin/bash
# Script généré automatiquement — exécuter en root (sudo) pour créer les comptes

useradd -m -s /bin/bash -c "Mathis Harboux" -p '$6$u.coRRrAEijKaqKV$p/iQl2Ld/e0JnkiEPQ5S.3TNQiOwmdYD9JS6qOMte1z2kgdKZ3c8pC5IsGqiwxuWXBhTM.HrG5rwHdgGcJJdK/' mharboux || echo 'Échec useradd mharboux'
chage -d 0 mharboux || true
useradd -m -s /bin/bash -c "Lucas Delgehier" -p '$6$2pDF.U8F7ZRMZ8Gb$/Pb5e/1l78EMIrGn2VCynS.lGApcHP.XSzhKTPlBkD3KaV4zdeRLW/7pdNCvpdbSE.ocb7QP7zMdUZVJkss291' ldelgehier || echo 'Échec useradd ldelgehier'
chage -d 0 ldelgehier || true
useradd -m -s /bin/bash -c "Sosthene Toviekou" -p '$6$Lf3spWhtlf.MGqAc$IkbgjKSteU.spZEUTw1q/uW9ILpcUmi.asfOngqQkrxz.U6.COWvaKEhG8RDWgNipvi.wTqRfKrIyK3YBlRGA1' stoviekou || echo 'Échec useradd stoviekou'
chage -d 0 stoviekou || true
