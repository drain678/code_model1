"""Tests for first homework on greetings."""
import pytest

from hw1 import say_hello

defaul_en = 'Hello'
test_greetings = (
    ('ru', 'Здравствуйте'),
    ('en', 'Hello'),
    ('es', 'Hola'),
    ('akjsdhlsadl', 'Hello'),
    ('asdsad', defaul_en),
    ('qweqweqw', defaul_en),
    ('trhrhr', defaul_en),
    ('asdsad', defaul_en),
    ('zvxcv', defaul_en),
)


@pytest.mark.parametrize('lang, expected', test_greetings)
def test_say_hello(lang: str, expected: str) -> None:
    """Test say_hello function with expected greetings using assertion.

    Args:
        lang: a given language.
        expected: a greeting by given language.
    """
    assert all((say_hello(lang), expected))
