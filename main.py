import rotator
from rotator import word_rotator_core as r_func


try:
	print(r_func(False))
	# print(r_func(input("Enter a sentence or a word: ")))

except rotator.WRCoreException as err:
	print(err)

# TODO 1. throwing exception in word_rotator_core() method
# TODO 2. capital letter detector
# TODO 3. cyclic input from the CLI (prompt: ri| )
# TODO 4. redirect i/o from/to file.txt
