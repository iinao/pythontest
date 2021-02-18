from http_pyynto import hae_postinumerot

def ryhmittele_toimipaikkoihin(postinumerot):
    toimipaikat = {}
    for numero, tmp in postinumerot.items():
        tmp = tmp.replace("-","").replace(" ","")
        if tmp in toimipaikat:
            toimipaikat[tmp].append(numero)
        else:
            toimipaikat[tmp] = [numero]

    return toimipaikat


def etsi_toimipaikan_numerot(haettava):
    postinumerot = hae_postinumerot()
    toimipaikat = ryhmittele_toimipaikkoihin(postinumerot)
    muotoiltu = haettava.strip().upper().replace("-","").replace(" ","")
    if muotoiltu == "SMARTPOST" or muotoiltu == "SMARTPSOT":
        lista = toimipaikat["SMARTPOST"] + toimipaikat["SMARTPSOT"]
        return lista
    elif muotoiltu in toimipaikat:
        return toimipaikat[muotoiltu]
    else:
        return []


def muotoile_tuloste(numerot):
    if numerot:
        return 'Postinumerot: ' + ', '.join(numerot)
    else:
        return 'Postitoimipaikkaa ei löytynyt'


def main():
    

    haettava = input('Kirjoita postitoimipaikka: ')

    numerot = sorted(etsi_toimipaikan_numerot(haettava))

    tuloste = muotoile_tuloste(numerot)

    print(tuloste)


if __name__ == '__main__':
    main()