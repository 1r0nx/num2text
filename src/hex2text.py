#!/usr/bin/python3

import argparse
import re

def hex_to_text(hex_string):
    tokens = re.findall(r'0x[0-9a-fA-F]{1,2}|[0-9a-fA-F]{2}|[0-9a-fA-F]{1}', hex_string)
    bytes_list = []
    for t in tokens:
        if t.lower().startswith('0x'):
            h = t[2:]
        else:
            h = t
        if len(h) == 1:
            h = '0' + h
        bytes_list.append(h)
    hex_clean = ''.join(bytes_list)
    return bytes.fromhex(hex_clean).decode('utf-8', errors='replace')

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="convert hex to text. ex: \"0x48 0x65 0x6C 0x6C 0x6F\" or \"48 65 6C 6C 6F\" or \"48656c6c6f\"")
	parser.add_argument('-s', '--string', type=str, metavar="string", help='string of hex numbers separed by spaces. ex: "48 65 6C 6C 6F" with the quotes')
	parser.add_argument('-f', '--file', type=str, metavar="filename", help='filename with the hex numbers separed by spaces. ex: "48 65 6C 6C 6F" without the quotes')
	args = parser.parse_args()

	if args.string != None:
		res = hex_to_text(args.string)
		print(res)

	elif args.file != None:
		file = args.file
		with open(file, "r") as f:
			content = f.read()
		res = hex_to_text(content)
		print(res)

	else:
		parser.print_help()