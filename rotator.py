class WRCoreException(TypeError):
    """Výjimka pro word_rotator_core při špatném typu vstupu."""
    pass


def word_rotator_core(text: str) -> str:
    """
    Otočí písmena v každém slově (slovo = souvislá sekvence písmen).
    Interpunkci a mezery ponechá na místě.

    Pravidla velikosti písmen:
    - 'AGI' -> 'IGA' (zůstane ALL CAPS)
    - 'Nexi' -> 'Ixen' (zůstane Capitalized)
    - 'dáváš' -> 'šávád' (zůstane lowercase)
    """
    if not isinstance(text, str):
        raise WRCoreException(f"Word rotator core exception: {text!r} is not a string!")

    result: list[str] = []
    i = 0
    n = len(text)

    while i < n:
        ch = text[i]

        # Slovo = souvislá sekvence písmen (funguje i pro diakritiku)
        if ch.isalpha():
            j = i
            while j < n and text[j].isalpha():
                j += 1

            word = text[i:j]
            reversed_word = word[::-1]

            # Zachování stylu velikosti písmen
            if word.isupper():
                reversed_word = reversed_word.upper()
            elif word[0].isupper():
                reversed_word = reversed_word.lower().capitalize()
            else:
                reversed_word = reversed_word.lower()

            result.append(reversed_word)
            i = j
        else:
            # Interpunkce, mezery, čísla… necháváme jak jsou
            result.append(ch)
            i += 1

    return "".join(result)
