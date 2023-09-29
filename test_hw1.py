"""Tests for first homework on greetings."""
import pytest

from hw1 import say_hello

test_greetings = (
    ('ru', 'Здравствуйте'),
    ('en', 'Hello'),
    ('es', 'Hola'),
    ('akjsdhlsadl', 'Hello'),
)


@pytest.mark.parametrize('lang, expected', test_greetings)
def test_say_hello(lang: str, expected: str) -> None:
    """Test say_hello function with expected greetings using assertion.

    Args:
        lang: a given language.
        expected: a greeting by given language.
    """
    assert say_hello(lang) == expected
