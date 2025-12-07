#!/usr/bin/python3

import argparse
import re

def ascii_to_text(s):
    cleaned = re.sub(r'[^0-9]', ' ', s)
    return ''.join(chr(int(code)) for code in cleaned.split())

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="convert ascii to text.")
	parser.add_argument('-s', '--string', type=str, metavar="string", help='string of ascii numbers separed by spaces. Ex: "72 101 108 108 111" with the quotes')
	parser.add_argument('-f', '--file', type=str, metavar="filename", help='filename with the ascii numbers separed by spaces. Ex: "72 101 108 108 111" without the quotes')
	args = parser.parse_args()

	if args.string != None:
		res = ascii_to_text(args.string)
		print(res)

	elif args.file != None:
		file = args.file
		with open(file, "r") as f:
			content = f.read()
		res = ascii_to_text(content)
		print(res)

	else:
		parser.print_help()

