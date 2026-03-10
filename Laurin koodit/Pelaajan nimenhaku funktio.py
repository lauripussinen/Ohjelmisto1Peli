def hae_pelaajan_peli(nimi):
    sql = 'SELECT * FROM game WHERE screen_name = %s ORDER BY id DESC LIMIT 1'
    cursor = yhteys.cursor(dictionary=True)
    cursor.execute(sql, (nimi,))
    return cursor.fetchone()