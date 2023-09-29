"""Greetings in different languages."""


def say_hello(lang: str) -> str:
    """Get greeting in a given language.

    Args:
        lang: a given language.

    Returns:
        str: a greeting in a language, defaults to 'Hello'.
    """
    greetings = {
        'ru': 'Здравствуйте',
        'en': 'Hello',
        'es': 'Hola',
        'fr': 'Salut',
        'cn': 'Ni hao',
    }
    greeting = greetings.get(lang)
    return greeting if greeting else 'Hello'
