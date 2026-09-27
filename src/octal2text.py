#!/usr/bin/python3

import argparse
import re
import sys


def _decode(vals):
    """Decode a list of byte values to text: UTF-8 if valid, else latin-1
    (which maps every byte, so this never fails)."""
    raw = bytes(vals)
    try:
        return raw.decode('utf-8')
    except UnicodeDecodeError:
        return raw.decode('latin-1')


def octal_to_text(octal_string):
    """Convert octal byte values (with or without separators or '0o' prefix)
    to text. Tokens outside the byte range 0-255 (e.g. octal > 377) are skipped
    so noisy input never crashes the tool."""
    vals = []
    for t in re.findall(r'0o[0-7]{1,3}|[0-7]{1,3}', octal_string):
        o = t[2:] if t.lower().startswith('0o') else t
        v = int(o, 8)
        if 0 <= v <= 255:
            vals.append(v)
    return _decode(vals)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="convert octal to text. ex: \"0o110 0o145 0o154 0o154 0o157\" or \"110 145 154 154 157\" or \"110145154154157\"")
    parser.add_argument('-s', '--string', type=str, metavar="string", help='octal numbers separated by spaces. ex: "110 145 154 154 157" with the quotes')
    parser.add_argument('-f', '--file', type=str, metavar="filename", help='file containing the octal numbers separated by spaces')
    args = parser.parse_args()

    if args.string is not None:
        data = args.string
    elif args.file is not None:
        try:
            with open(args.file) as f:
                data = f.read()
        except OSError as e:
            print(f"[!] cannot read file: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        parser.print_help()
        sys.exit(0)

    print(octal_to_text(data))
