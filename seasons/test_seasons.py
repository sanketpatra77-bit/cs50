from seasons import to_words

def test_get_words():
    assert to_words(525600) == "Five hundred twenty-five thousand, six hundred minutes"
    assert to_words(527040) == "Five hundred twenty-seven thousand forty minutes"