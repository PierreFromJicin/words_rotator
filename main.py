import rotator
from rotator import word_rotator_core as r_func

try:
	# print(r_func(False))
	next_s: bool = True
	str_in: str = ''
	while next_s is True:
		print(r_func(input("Write your word or a sentence: ")))
		str_in = input("To stop the rotator write 'stop', to switch rotator into file write 'file', "
					   "to continue press Enter.: ")
		if str_in == "stop":
			next_s = False
		if str_in == "file":
			data_results = []
			with open("./input_files/input_file.txt", encoding='utf-8') as data_rotator:
				for item in data_rotator.readlines():
					line_string = str(item)
					data_results.append(r_func(line_string) + '\n')

			with open("./output_files/output_file.txt", 'w', encoding='utf-8') as output:
				output.write(''.join([str(item) for item in data_results]))
	print("The game is over :)")

except rotator.WRCoreException as err:
	print(err)
