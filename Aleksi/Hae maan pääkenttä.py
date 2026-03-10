def hae_maan_paakentta(maa):
    sql = 'SELECT airport.ident FROM airport WHERE iso_country = %s ORDER BY type = "large_airport" DESC LIMIT 1'
    cursor = yhteys.cursor()
    cursor.execute(sql, (maa,))
    tulos = cursor.fetchone()
    return tulos[0] if tulos else None