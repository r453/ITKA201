#/usr/bin/python3
# Tehtävä 4 (a) https://studyguide.jyu.fi/2026/en/courseunit/itka201/
#
# Annettuna on taulukko, jossa on kokonaislukuja satunnaisessa järjestyksessä.
# Suunnittele algoritmi, joka etsii taulukon pienimmän alkion.
#
# Author afmansne https://github.com/r453
# Lisenssi CC0 (vapaasti käytettävä)

def hae_pienin_alkio(taulukko):
    if len(taulukko) == 0:
        raise ValueError("ERROR: Taulukko on tyhjä")

    pienin = taulukko[0]           # oletetaan ensimmäinen luku pienimmäksi
    for i in range(1, len(taulukko)):
        if taulukko[i] < pienin:   # löytyi pienempi, päivitetään pienin
            pienin = taulukko[i]
    return pienin		   # kaikki tarkastettu, palautetaan pienin

if __name__ == "__main__":
    luvut = [7, 3, 9, -2, 15, 0, 4, 12]
    print(f"Taulukon {luvut} pienin luku on {hae_pienin_alkio(luvut)}")
