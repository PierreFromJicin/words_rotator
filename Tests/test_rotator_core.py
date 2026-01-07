import pytest
from rotator import word_rotator_core, WRCoreException


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Nexi, Ty mi dáváš kapky!", "Ixen, Yt im šávád ykpak!"),
        (" Ten kód jsem psal já, kámo.", " Net dók mesj lasp áj, omák."),
        (" Ale díky za zhodnocení.", " Ela ykíd az ínecondohz."),
        (" Jsem rád že mohu využít pomoc AGI.", " Mesj dár ež uhom tížuyv comop IGA."),
    ],
)
def test_rotate_sentences(text, expected):
    assert word_rotator_core(text) == expected


def test_preserves_leading_spaces():
    # edukativní: split() by tuhle mezeru zabilo, my ji chceme zachovat
    assert word_rotator_core("  Ahoj")[:2] == "  "


def test_all_caps_word_stays_all_caps():
    assert word_rotator_core("AGI") == "IGA"


def test_capitalized_word_stays_capitalized():
    assert word_rotator_core("Nexi") == "Ixen"


def test_lowercase_stays_lowercase():
    assert word_rotator_core("dáváš") == "šávád"


def test_raises_custom_exception_on_non_string():
    with pytest.raises(WRCoreException) as excinfo:
        word_rotator_core(False)

    # edukativní: ověř i message, ať víš, že exception nese informaci
    assert "is not a string" in str(excinfo.value)
