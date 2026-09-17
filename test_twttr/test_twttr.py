from twttr import shorten

def test_shorten():
    assert shorten("Sanket") == "Snkt"

def test_no_vaules():
    assert shorten("CS50") == "CS50"

def test_only_vaules():
    assert shorten("aeiou") == ""