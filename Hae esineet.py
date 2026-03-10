def hae_esineet():
    cursor = yhteys.cursor(dictionary=True)
    cursor.execute("SELECT * FROM item")
    return cursor.fetchall()