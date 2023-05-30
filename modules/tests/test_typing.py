import pytest

from modules import typing

@pytest.fixture(autouse=True)
def tm():
    return typing.TypingModule()

def test_line_split(tm):
    for line in tm._split_lines():
        assert sum(len(word) for word in line) <= 60

def test_validate_word(tm):
    t_word = tm._lines[0][0]

    assert tm._validate_word(t_word, 0, 0)
    assert tm._validate_word(t_word + '_', 0, 0) == False
