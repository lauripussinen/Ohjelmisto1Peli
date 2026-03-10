#funktion käyttö jäi hieman ennen esitystä pieneksi, kun sen päätarkoitukseen olisi pitänyt tehdä isoja muutoksia lennä
#ja tallenna funktioihin sekä tietokantaan
def hae_maan_nimi(iso_koodi):
    sql = 'SELECT name FROM country WHERE iso_country = %s'
    cursor = yhteys.cursor(dictionary=True)
    cursor.execute(sql, [iso_koodi])
    tulos = cursor.fetchone()
    cursor.close()
    return tulos["name"]
