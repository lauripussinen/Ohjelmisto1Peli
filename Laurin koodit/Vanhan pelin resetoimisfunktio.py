def resetoi_peli(game_id, aloitus_icao, difficulty):
    sql = 'UPDATE game SET location=%s, co2_consumed=0, current_item=0, attempts=0, difficulty=%s WHERE id=%s'
    cursor = yhteys.cursor()
    cursor.execute(sql, (aloitus_icao, difficulty, game_id))
    yhteys.commit()
    cursor.close()