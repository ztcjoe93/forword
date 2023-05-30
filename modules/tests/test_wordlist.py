import pytest
from modules import wordlist

@pytest.fixture(autouse=True)
def wl():
    return wordlist.WordList()

def test_generate_words(wl):
    for num in [5, 20, 100]:
        assert len(wl.generate_words(num)) == num

def test_wl_dict_count(wl):
    assert len(wl._dict) == 901