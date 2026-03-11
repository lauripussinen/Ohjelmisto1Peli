def hae_pelaajan_peli(nimi):
    cursor = yhteys.cursor(dictionary=True)
    cursor.execute('SELECT * FROM game WHERE screen_name = %s ORDER BY id DESC LIMIT 1', [nimi])
    return cursor.fetchone()