#!/usr/bin/python3

import argparse
import re

def octal_to_text(octal_string):
    """
    Convertit une string contenant des codes octaux (avec ou sans séparateurs, ou avec '0o')
    en texte UTF-8.
    """
    # Trouve soit "0oXYZ" soit des groupes de 1 à 3 chiffres octaux
    tokens = re.findall(r'0o[0-7]{1,3}|[0-7]{1,3}', octal_string)
    bytes_list = []

    for t in tokens:
        # Retire le préfixe 0o
        if t.lower().startswith("0o"):
            o = t[2:]
        else:
            o = t

        # Complète à 3 chiffres (car 1 octet = 3 chiffres en octal max : 000 → 377 octal)
        o = o.zfill(3)

        # Convertit en entier et ajoute comme octet
        bytes_list.append(int(o, 8))

    return bytes(bytes_list).decode("utf-8", errors="replace")

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="convert octal to text. ex: \"0o110 0o145 0o154 0o154 0o157\" or \"110 145 154 154 157\" or \"110145154154157\"")
	parser.add_argument('-s', '--string', type=str, metavar="string", help='string of octal numbers separed by spaces. ex: "110 145 154 154 157" with the quotes')
	parser.add_argument('-f', '--file', type=str, metavar="filename", help='filename with the octal numbers separed by spaces. ex: "110 145 154 154 157" without the quotes')
	args = parser.parse_args()

	if args.string != None:
		res = octal_to_text(args.string)
		print(res)

	elif args.file != None:
		file = args.file
		with open(file, "r") as f:
			content = f.read()
		res = octal_to_text(content)
		print(res)

	else:
		parser.print_help()