#tuo Tarinat-tiedostosta peliin erinäisiä tekstejä
import Tarinat

#oikean esineen löydyttä sankirjasta tulostuu oikea esineen tarina Tarinat-tiedostosta.
tarina_funktiot = {
    "Kirje": Tarinat.kirje,
    "Kultainen teelusikka": Tarinat.teelusikka,
    "Kaulakoru": Tarinat.kaulakoru,
    "Nahkahanskat": Tarinat.nahkahanskat,
    "Taskukello": Tarinat.taskukello
}

#luo pelin alussa johdantotarinan
for rivi in Tarinat.johdanto():
        print(rivi)

#pääohjelmassa, jos pelaaja haluaa tehdö jo luodulle pelaajalle uuden pelin
else:
    for rivi in Tarinat.johdanto():
        print(rivi)
    print("Peli alkaa! CO2-budjetti: 5000")
    aloitus = 'EFHK'
    difficulty = input("Valitse vaikeustaso (HELPPO/KESKIVAIKEA/VAIKEA): ").upper()
    resetoi_peli(vanha_peli["id"], aloitus, difficulty)
    game_id = vanha_peli["id"]