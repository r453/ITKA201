#/usr/bin/python3
# 
# Tehtävä 6 https://tim.jyu.fi/view/kurssit/tie/itka201/2026s/demot/D2#a1k21o1
#
# Kirjoita ohjelma, jolla voidaan laskea, kuinka moni kokonaislukutaulukon 
# alkioista on jaollinen annetulla luvulla m. Muodosta taulukko, joka sisältää 
# satunnaisia kokonaislukuja, ja laske kuinka moni sen luvuista on jaollinen 
# luvuilla m=2, m=3 ja m=5.
# 
# Ohjelmointitehtävän ohjeita:
#
# Toteuta jokainen operaatio tai muu vastaava tehtäväkokonaisuus erillisessä 
# aliohjelmassa.
#
# Kirjoita pääohjelmaan riittävä määrä aliohjelmien testikutsuja sekä 
# testitulostuksia näytölle.
#
# Suunnittele tulostukset siten, että niiden perusteella voi nähdä suoraan, 
# toimiiko ohjelma oikein.
#
# Testitulostukset voi tällä opintojaksolla toteuttaa tulostamalla aliohjelmien 
# tulokset näytölle (käyttämällä rutiineja print, Console.Write yms.) eli ei 
# tarvitse kirjoittaa automaattitestejä.
#
# Author afmansne https://github.com/r453/ITKA201
# Lisenssi CC0 (vapaasti käytettävä)

import random

# Taulukko
taulukko=[]
# Lista arvoista m
m_values = [2, 3, 5]
n=0 # apumuuttuja löydösten laskemiseksi

# Muodosta taulukko, jossa on n kpl satunnaisia kokonaislukuja
def muodosta_taulukko():
    n = 15
    taulukko = random.sample(range(1, 101), n)
    print(f"[DEBUG] Muodostettu taulukko {(taulukko)}")             # testikutsu
    print(f"[DEBUG] Funktio muodosta_taulukko() ajettu")# testikutsu
    return taulukko 

# Tarkasta taulukon koko jos kutsutaan toisesta ohjelmasta
def tarkasta_taulukon_koko(taulukko):
    print(f"[DEBUG] Aloitetaan taulukon koon tarkastus")             # testikutsu
    if len(taulukko) == 0:
        return 0
    return 1

# Aliohjelma, jolle annetaan parametrina taulukko, m ja n
def tutki_jaollisuus(taulukko,m,n):
    print(f"[DEBUG] Aloitetaan jaollisuuden tarkastus arvolla {m} ja taulukolla {taulukko}") # testikutsu
    for i in range(0, len(taulukko)):
        # print(f"[DEBUG] tutki_jaollisuus silmukassa arvolla {i}") # testikutsu
        if taulukko[i] %m ==0:     # lasketaan alkion jaollisuus luvulla m
            print(f"[DEBUG] Löydös: {taulukko[i]}") # testikutsu
            n +=1
    print(f"[DEBUG] n={n}") # testikutsu
    return n		           # kaikki tarkastettu, palautetaan löydösten määrä

if __name__ == "__main__":
    taulukko = muodosta_taulukko()
    print(f"[DEBUG] Saatu funktiolta taulukko {taulukko}")# testikutsu
    tarkasta_taulukon_koko(taulukko)
    for m in m_values:
        n=0
        n=tutki_jaollisuus(taulukko, m,n)
        if n == 1:
            print(f"Taulukon {taulukko} alkioista {n} on jaollinen luvulla {m}")
        elif n > 1:
            print(f"Taulukon {taulukko} alkioista {n} on jaollisia luvulla {m}")
        else:
            print(f"Taulukon {taulukko} alkiot eivät ole jaollisia luvulla {m}")
