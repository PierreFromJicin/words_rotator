import rotator
from rotator import word_rotator_core as r_func

try:
	# print(r_func(False))
	next_s: bool = False
	str_in: str =''
	while next_s is False:
		print(r_func(input("Write your word or a sentence: ")))
		str_in = input("To stop the rotator write 'stop', to continue press Enter.: ")
		if str_in == "stop":
			next_s = True

except rotator.WRCoreException as err:
	print(err)
