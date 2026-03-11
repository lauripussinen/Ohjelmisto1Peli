#ei käyetty pelin lopullisessa versiossa
#tunnuksen luominen toimii, mutta tarkistaminen ei

import mysql.connector

yhteys = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='tunnukset',
    user='root',
    password='Akita68',
    autocommit=True
)


def lisaa_tunnus(uusi_tunnus):

    sql = "INSERT INTO users (nimi) VALUES (%s);"

    kursori = yhteys.cursor()
    kursori.execute(sql, (uusi_tunnus,))
    print(f"Tunnus '{uusi_tunnus}' lisätty!")


def tarkista_tunnus(vanha_tunnus):
    sql2 = "SELECT * from users where nimi = (jatka_peli);"
    kursori2 = yhteys.cursor()
    kursori2.execute(sql2, (jatka_peli,))
    print(f"Tunnus '{jatka_peli}' löytyi!")


print("Tervetuloa peliin!")
print("Voit aloittaa uuden pelin luomalla uuden käyttäjätunnuksen,\ntai jatkaa aikaisemmin aloittamaasi peliä syöttämällä vanhan käyttäjäätunnuksesi")
uusitaijatka = int(input("Valitse\n'1' aloittaaksesi uuden peli\n'2' jatkaaksesi\n "))
if uusitaijatka == 1:
    uusi_tunnus = input("Anna uusi tunnus: ")
    lisaa_tunnus(uusi_tunnus)
elif uusitaijatka == 2:
    jatka_peli = input("Mikä on nimesi: ")
    if jatka_peli:
        tarkista_tunnus(jatka_peli)
