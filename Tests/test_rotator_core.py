import pytest
from main import rotator_core


def test_rotator_core_positive():
	assert rotator_core("This is testing sentence.") == "Ecnetnes gnitset si siht."
