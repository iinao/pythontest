from postinumerot import ryhmittele_toimipaikkoihin, etsi_toimipaikan_numerot, muotoile_tuloste


def test_ryhmittele_yksi_postinumero():
    aineisto = {"92140": "PATTIJOKI"}

    toimipaikat = ryhmittele_toimipaikkoihin(aineisto)

    assert toimipaikat == {"PATTIJOKI": ["92140"]}


def test_ryhmittele_useita_postinumeroita():
    aineisto = {
    "74701": "KIURUVESI",
    "35540": "JUUPAJOKI",
    "74700": "KIURUVESI",
    "73460": "MUURUVESI",
    "43800": "KIVIJÄRVI",
    "91150": "YLI-OLHAVA",
    "65374": "SMART POST"
    }

    toimipaikat = ryhmittele_toimipaikkoihin(aineisto)

    assert toimipaikat == {
        "KIURUVESI": ["74701", "74700"],
        "JUUPAJOKI": ["35540"],
        "MUURUVESI": ["73460"],
        "KIVIJÄRVI": ["43800"],
        "YLIOLHAVA": ["91150"],
        "SMARTPOST": ["65374"]
    }


def test_etsi_toimipaikan_numero():
    toimipaikat ={}
    assert etsi_toimipaikan_numerot("PATTIJOKI") == ["92140"]

def test_etsi_toimipaikan_numerot():
    toimipaikat ={}

    assert etsi_toimipaikan_numerot("INKOO") == ["10211", "10210"]


def test_etsi_olemattoman_toimipaikan_numerot():
    toimipaikat ={}

    assert etsi_toimipaikan_numerot("BERLIINI") == []

def test_etsi_toimipaikan_numerot_eri_kirjoitusasuilla():
    toimipaikat = {}

    assert etsi_toimipaikan_numerot("TÄHTELÄ") == ["10120"]
    assert etsi_toimipaikan_numerot("tähtelä") == ["10120"]
    assert etsi_toimipaikan_numerot("Tähtelä") == ["10120"]
    assert etsi_toimipaikan_numerot("TäHTelä") == ["10120"]

def test_smart_post_muotoilu():
    toimipaikat = {}
    
    assert etsi_toimipaikan_numerot("SMARTPOST") == etsi_toimipaikan_numerot("SMART POST")
    assert etsi_toimipaikan_numerot("SMARTPOST") == etsi_toimipaikan_numerot("SMART-POST")
    assert etsi_toimipaikan_numerot("SMARTPOST") == etsi_toimipaikan_numerot("SMARTPSOT")

    

def test_muotoile_tuloste_tyhjalle_listalle():
    tuloste = muotoile_tuloste([])

    assert 'ei löytynyt' in tuloste


def test_muotoile_tuloste_monelle_postinumerolle():
    tuloste = muotoile_tuloste(['00100', '00280'])

    assert '00100, 00280' in tuloste
