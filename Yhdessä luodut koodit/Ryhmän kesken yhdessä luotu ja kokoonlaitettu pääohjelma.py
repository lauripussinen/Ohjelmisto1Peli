#pääohjelma on luotu kokoon ryhmän kesken tunneilla ja palavereissa

#Peli alkaa
nimi = input("Anna pelaajan nimi: ")
vanha_peli = hae_pelaajan_peli(nimi)


if vanha_peli:
    print(f"Löydettiin tallennettu peli pelaajalle {nimi}.")
    print(f"Nykyinen maa: {vanha_peli['location']}")
    print(f"CO2-kulutus: {vanha_peli['co2_consumed']} / {vanha_peli['co2_budget']}")
    print(f"Löydettyjä mummon esineitä: {vanha_peli['current_item']}")
    print(f"Vaikeustaso: {vanha_peli['difficulty']}")
    jatka = input("Haluatko jatkaa tallennettua peliä? (KYLLÄ/EN): ").upper()
    if jatka == "KYLLÄ":
        game_id = vanha_peli["id"]
        print(f"Peli jatkuu! Olet kuluttanut CO2:sta {vanha_peli['co2_consumed']}. Muista, että budjetti on 5000!")
    else:
        for rivi in Tarinat.johdanto():
            print(rivi)
        print("Peli alkaa! CO2-budjetti: 5000")
        aloitus = 'EFHK'
        difficulty = input("Valitse vaikeustaso (HELPPO/KESKIVAIKEA/VAIKEA): ").upper()
        resetoi_peli(vanha_peli["id"], aloitus, difficulty)
        game_id = vanha_peli["id"]
else:
    for rivi in Tarinat.johdanto():
        print(rivi)
    print("Peli alkaa! CO2‑budjetti: 5000")
    aloitus = 'EFHK'
    difficulty = input("Valitse vaikeustaso (HELPPO/KESKIVAIKEA/VAIKEA): ").upper()
    game_id = luo_peli(nimi, aloitus, difficulty)
esineet = hae_esineet()

# Pelin silmukka
peli_ohi = False
while peli_ohi == False:
    peli_tila = hae_peli(game_id)

    #Kaikki esineet löydetty ja peli päättyy voittoon.
    if peli_tila["current_item"] >= len(esineet):
        print("Onneksi olkoon, olet löytänyt kaikki mummon hävittäneet esineet. Mummosi on sinulle ikuisesti kiitollinen.")
        peli_ohi = True
        continue

    esine = esineet[peli_tila["current_item"]]
    print("Vihje:", anna_vihje(esine, peli_tila["attempts"]))
    maan_nimi = input("Mihin maahan haluat lentää? ")
    pelaajan_maa = hae_maan_iso_koodi(maan_nimi)
    if not pelaajan_maa:
        print("Tuntematon maa. Syötä haluamasi maa uudelleen.")
        continue

    tila = lenna(game_id, pelaajan_maa)

    if tila == 'peli loppuu':
        print("Peli loppui, koska ylitit mummon antaman CO2-budjetin. Mummo on nyt pettynyt sinuun.")
        peli_ohi = True
        continue

    tarkista_esine(game_id, pelaajan_maa, esineet)