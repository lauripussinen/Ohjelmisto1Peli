def lenna(game_id, kohde_maa):
    peli = hae_peli(game_id)
    nykyinen_icao = peli["location"]
    kohde_icao = hae_maan_paakentta(kohde_maa)
    if kohde_icao is None:
        print("Tuntematon maa. Syötä haluamasi maa uudestaan.")
        return

    km = etaisyys(nykyinen_icao, kohde_icao)
    paasto = vaikeustaso(km, peli["difficulty"])
    uusi_kulutus = peli["co2_consumed"] + paasto
    if uusi_kulutus > peli["co2_budget"]:
        paivita_peli(game_id, kohde_icao, uusi_kulutus, peli["current_item"], peli["attempts"], peli["difficulty"])
        print(f"CO2-budjetti ylittyi ({uusi_kulutus:.1f} / {peli['co2_budget']})! Peli loppuu.")
        return "peli loppuu"


    maan_nimi = hae_maan_nimi(kohde_maa)
    print(f"Lensit maahan {maan_nimi} ({km:.1f} km)")
    print(f"CO2 yhteensä: {uusi_kulutus:.1f} / {peli['co2_budget']}")
    paivita_peli(game_id, kohde_icao, uusi_kulutus, peli["current_item"], peli["attempts"], peli["difficulty"])
    return