organizacja = {
"sklep": {
        "owoce": {
            "pomarancze":{"cena": 5, "ilosc": 6},
            "jabka": {"cena": 3, "ilosc": 5},
            "banan": {"cena": 7, "ilosc": 66}
            },
        "warzywa": {
            "ziemniok": {"cena": 1, "ilosc": 1000}
            }
        },
"magazyn": {}
}

def parametry_produktu(organizacja, docelowy_produkt):
    '''funkcja ktora zwraca parametry (cena, ilosc), przy wejsciowych paramteryach typu produkt'''
    for rodzaj_struktury in organizacja:
        print rodzaj_struktury , 'rodzaj struktury'
        for typ_produktu in organizacja[rodzaj_struktury]:
            print typ_produktu , 'typ produktu'
            for produkt in organizacja[rodzaj_struktury][typ_produktu]:
                print produkt
                if docelowy_produkt == produkt:
                    print organizacja[rodzaj_struktury][typ_produktu][docelowy_produkt]["cena"]
                    print organizacja[rodzaj_struktury][typ_produktu][docelowy_produkt]["ilosc"]

