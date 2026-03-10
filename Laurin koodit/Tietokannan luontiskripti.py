# 1. Luo aluksi uusi tietokanta.
create database ohjelmistopeli;

#2. Käytä uutta luotua tietokantaa.
use ohjelmistopeli;

#3. Lisää tietokantaan sql tiedosto, jota on käytetty flight_game-tietokannassa.
# Minulla tiedosto löytyy tietokoneen C-levyltä o1 kansiosta lp1.sql nimellä.
source C:\o1\lp1.sql;

#4. Poistetaan tuodusta qsl-tiedostosta game, goal ja goal_reached-taulut.
SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS game;
DROP TABLE IF EXISTS goal;
DROP TABLE IF EXISTS goal_reached;
SET FOREIGN_KEY_CHECKS = 1;

#5. Luodaan ensiksi uusi game-taulu.
CREATE TABLE game (
    id int auto_increment primary key,
    screen_name varchar(40) NOT NULL UNIQUE,
    location varchar(40) NOT NULL,
    co2_consumed float default 0,
    co2_budget float default 5000,
    current_item int default 0,
    attempts int default 0,
    difficulty varchar(40) NOT NULL
)
charset=latin1;

#6. Luodaan lopuksi oma item-taulu.
create table item (
      id int auto_increment primary key,
      nimi         varchar(100) null,
	  maa          varchar(40)  null,
      vihje1       varchar(255) null,
      vihje2       varchar(255) null,
      vihje3       varchar(255) null
)
	charset=latin1;

#7. Lisätään Aleksin arvot item tauluun.
INSERT INTO item (nimi, maa, vihje1, vihje2, vihje3) VALUES
(
    'Kultainen teelusikka',
    'SE',
    'Kultainen teelusikka sijaitsee maassa, joka tunnetaan kolmesta kruunusta.',
    'Kultainen teelusikka sijaitsee maassa, jossa on paremmat lihapullat.',
    'Kultainen teelusikka sijaitsee maassa, jossa juhlitaan keskikesän juhlaa.'
),
(
    'Taskukello',
    'IT',
    'Taskukello sijaitsee maassa, jossa Egyptin prinssi syntyi.',
    'Taskukello sijaitsee maassa, joka tunnetaan eräästä diktaattorista.',
    'Taskukello sijaitsee maassa, jossa syödään pizzaa ja pastaa.'
),
(
    'Kaulakoru',
    'GB',
    'Kaulakoru sijaitsee maassa, jossa sinua tarkkaillaan jatkuvasti.',
    'Kaulakoru sijaitsee maassa, jossa sää on yleensä kamala.',
    'Kaulakoru sijaitsee maassa, jossa juodaan paljon teetä.'
),
(
    'Nahkahanskat',
    'FR',
    'Nahkahanskat sijaitsevat maassa, jossa ilma savuaa.',
    'Nahkahanskat sijaitsevat maassa, johon kaikki haluavat matkustaa, mutta eivät pidä paikallisista.',
    'Nahkahanskat sijaitsevat maassa, jossa patonki ja croissantit ovat iso juttu.'
),
(
    'Kirje',
    'RO',
    'Kirje sijaitsee maassa, jossa jokainen ajaa vanhalla mersulla.',
    'Kirje sijaitsee maassa, joka on hyvin köyhä.',
    'Kirje sijaitsee maassa, mistä Dracula on kotoisin.'
);

#8. Tarkistetaan onko tietokanta halutun mukainen eli, että oikeat taulut löytyvät.
show tables;

#9. Jos ja kun tulostuu seuraavat taulut: airport, country, game ja items,
# on ryhmän 3 ohjelmistopeli-tietokanta luotu onnistuneesti.