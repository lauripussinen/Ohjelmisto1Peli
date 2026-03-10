#funktio hakee tietokannasta lentokentän nimen ja koordinaatit
def lentokentat(icao):
    sql = "SELECT ident, name, latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    cursor = yhteys.cursor(dictionary=True)
    cursor.execute(sql, (icao,))
    result = cursor.fetchone()
    return result