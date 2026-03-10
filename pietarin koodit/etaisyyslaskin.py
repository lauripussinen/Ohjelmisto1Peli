def etaisyys(icao1, icao2):
    kentta1 = lentokentat(icao1)
    kentta2 = lentokentat(icao2)
    p1 = (kentta1["latitude_deg"], kentta1["longitude_deg"])
    p2 = (kentta2["latitude_deg"], kentta2["longitude_deg"])

    return distance.distance(p1, p2).km