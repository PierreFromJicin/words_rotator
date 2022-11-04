import rotator
from rotator import word_rotator_core as r_func


try:
	# print(r_func(False))
	print(r_func(input("Enter a sentence or a word: ")))

except rotator.WRCoreException as err:
	print(err)
