#!/usr/bin/python3

import argparse

def bin_to_text(string):
	bins = string.split(" ")
	try:
		text = ''.join(chr(int(b, 2)) for b in bins)
	except:
		print(f"Cannot convert to text")
		exit(0)

	return text

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="convert binary to text.")
	parser.add_argument('-s', '--string', type=str, metavar="string", help='string of binary numbers separed by spaces. Ex: "1110000 1101001 1100011 1101111" with the quotes')
	parser.add_argument('-f', '--file', type=str, metavar="filename", help='filename with the binary numbers separed by spaces. Ex: "1110000 1101001 1100011 1101111" without the quotes')
	args = parser.parse_args()
	
	if args.file is not None:
		file = args.file
		try:
			with open(file, "r") as f:
				binary_str = f.read()
		except:
			print(f"The file \"{file}\" doesnt exist!")	
			exit(0)	
		print(bin_to_text(binary_str))

	elif args.string is not None:
		binary_str = args.string
		if binary_str == "":
			print("Empty string")
			exit(0)
		print(bin_to_text(binary_str))

	else:
		parser.print_help()
