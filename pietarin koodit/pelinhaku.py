def hae_peli(game_id):
    cursor = yhteys.cursor(dictionary=True)
    cursor.execute("SELECT * FROM game WHERE id = %s", (game_id,))
    return cursor.fetchone()