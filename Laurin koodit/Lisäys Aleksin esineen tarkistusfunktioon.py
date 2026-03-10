#esineen tarkistus funktioon lisäys, jotta esineen löydyttyä tulostuu sen tarina
if tarkista_maa(pelaajan_maa, esine):
    print("Löysit esineen:", esine["nimi"])
if esine["nimi"] in tarina_funktiot:
    for rivi in tarina_funktiot[esine["nimi"]]():
        print(rivi)