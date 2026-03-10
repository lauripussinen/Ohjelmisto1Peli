#luo uuden pelin
def luo_peli(nimi, aloitus_icao, difficulty):
    sql = 'INSERT INTO game (screen_name, location, co2_consumed, co2_budget, current_item, attempts, difficulty) VALUES (%s, %s, 0, 5000, 0, 0, %s)'
    cursor = yhteys.cursor()
    cursor.execute(sql, (nimi, aloitus_icao, difficulty))
    yhteys.commit()
    return cursor.lastrowid