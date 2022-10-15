from rotator import word_rotator_core


def test_word_rotator_core_positive():
	assert word_rotator_core("This is the testing sentence.") == "Siht si eht gnitset ecnetne."


def test_word_rotator_core_negative():
	assert word_rotator_core(7) is False
