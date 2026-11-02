#/usr/bin/python3
# Tehtävä 6 https://studyguide.jyu.fi/2026/en/courseunit/itka201/
#
# Tee ohjelma, joka toteuttaa Tehtävän 4 (a)-kohdan mukaisen algoritmin. 
# Testaa ohjelman toimintaa jollakin taulukolla niin, että testitaulukko 
# tulostetaan sekä taulukon pienimmän alkion. 
#
# Author afmansne https://github.com/r453/ITKA201
# Lisenssi CC0 (vapaasti käytettävä)

import random

# Muodostetaan ensin taulukko, jossa on satunnaisia kokonaislukuja
n = 15  # taulukon koko
taulukko = random.sample(range(1, 101), n)

# Muodostetaan aliohjelma, jolle taulukko annetaan parametrina.
def hae_pienin_alkio(taulukko):
    if len(taulukko) == 0:    # lisätty virheenkorjaus jos kutsutaan toisesta ohjelmasta ja taulukko on tyhjä
        raise ValueError("ERROR: Taulukko on tyhjä")

    pienin = taulukko[0]           # oletetaan ensimmäinen luku pienimmäksi
    for i in range(1, len(taulukko)):
        if taulukko[i] < pienin:   # löytyi pienempi, päivitetään pienin
            pienin = taulukko[i]
    return pienin		   # kaikki tarkastettu, palautetaan pienin

if __name__ == "__main__":
    # Pääohjelmassa tulostetaan taulukko ennen aliohjelmakutsua ja aliohjelmakutsun palauttama arvo.
    print(f"Taulukon {taulukko} pienin luku on {hae_pienin_alkio(taulukko)}")
