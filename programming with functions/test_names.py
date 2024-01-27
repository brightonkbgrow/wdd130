from names import make_full_name, \
    extract_family_name, extract_given_name

import pytest



def test_make_full_name():

    full_name = make_full_name("Grow, Brighton")
    assert isinstance(full_name, str)

    assert (make_full_name("Grow; Brighton")) == "Grow; Brighton"
    assert (make_full_name("Erickson; Cami")) == "Erickson; Cami"
    assert (make_full_name("Dever; Jence")) == "Dever; Jence"
    assert (make_full_name("Kleven; Josiah")) == "Kleven; Josiah"
    assert (make_full_name("Hendrickson; Bryson")) == "Hendrickson; Bryson"
    assert (make_full_name("Davis; Spencer")) == "Davis; Spencer"

def test_extract_family_name():

    name = extract_family_name("Grow; Brighton")
    assert isinstance(name, str)

    assert (extract_family_name("Grow; Brighton")) == "Grow"
    assert (extract_family_name("Erickson; Cami")) == "Erickson"
    assert (extract_family_name("Dever; Jence")) == "Dever"
    assert (extract_family_name("Kleven; Josiah")) == "Kleven"
    assert (extract_family_name("Hendrickson; Bryson")) == "Hendrickson"
    assert (extract_family_name("Davis; Spencer")) == "Davis"


def test_extract_given_name():

    given_name = extract_given_name("Grow, Brighton")
    assert isinstance(given_name, str)
    assert (extract_given_name("Grow; Brighton")) == "Brighton"
    assert (extract_given_name("Erickson; Cami")) == "Cami"
    assert (extract_given_name("Dever; Jence")) == "Jence"
    assert (extract_given_name("Kleven; Josiah")) == "Josiah"
    assert (extract_given_name("Hendrickson; Bryson")) == "Bryson"
    assert (extract_given_name("Davis; Spencer")) == "Spencer"


pytest.main(["-v", "--tb=line", "-rN", __file__])