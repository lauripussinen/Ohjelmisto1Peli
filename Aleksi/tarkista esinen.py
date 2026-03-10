
'def tarkista_esine(game_id, pelaajan_maa, esineet):
    peli = hae_peli(game_id)
    indeksi = peli["current_item"]
    yritykset = peli["attempts"]
    esine = esineet[indeksi]
    if tarkista_maa(pelaajan_maa, esine):
        print("Löysit esineen:", esine["nimi"])
        if esine["nimi"] in tarina_funktiot:
            for rivi in tarina_funktiot[esine["nimi"]]():
                print(rivi)
        paivita_peli(game_id, peli["location"], peli["co2_consumed"], indeksi + 1, 0, peli["difficulty"])
        return True
    else:
        print("Lensit väärään maahan, TOLLO!")
        print("Vihje:", anna_vihje(esine, yritykset))
        yritykset += 1
        paivita_peli(game_id, peli["location"], peli["co2_consumed"], indeksi, yritykset, peli["difficulty"])
        return False