from rotator import word_rotator_core


def test_word_rotator_core_positive():
	assert word_rotator_core("This is the testing sentence, with comma!") == "Siht si eht gnitset ecnetnes, htiw ammoc!"


def test_word_rotator_core_negative():
	assert word_rotator_core(7) == "WRC exception: 7 is not a string"
