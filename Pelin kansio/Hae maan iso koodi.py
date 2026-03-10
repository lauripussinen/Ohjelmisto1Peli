def hae_maan_iso_koodi(nimi):
    sql = 'SELECT iso_country FROM country WHERE name = %s'
    cursor = yhteys.cursor(dictionary=True)
    cursor.execute(sql, (nimi,))
    tulos = cursor.fetchone()
    cursor.close()
    if tulos:
        return tulos["iso_country"]