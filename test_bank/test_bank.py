from bank import value
def test_hello():
    assert value("hello") == 0

def test_h():
    assert value("h") == 20

def test_any_word():
    assert value("") == 100