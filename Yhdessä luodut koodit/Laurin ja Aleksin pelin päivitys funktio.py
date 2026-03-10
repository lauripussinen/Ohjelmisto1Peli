def paivita_peli(game_id, location, co2_consumed, current_item, attempts, difficulty):
    sql = 'UPDATE game SET location=%s, co2_consumed=%s, current_item=%s, attempts=%s, difficulty=%s WHERE id=%s'
    cursor = yhteys.cursor()
    cursor.execute(sql, (location, co2_consumed, current_item, attempts, difficulty, game_id))
    yhteys.commit()