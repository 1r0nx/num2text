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


def bin_to_text(binary_string):
    """Convert binary byte values (optionally 0b-prefixed, any whitespace or
    separator) to text. Tokens outside the byte range 0-255 are skipped so
    noisy input never crashes the tool."""
    vals = []
    for t in re.findall(r'0b[01]+|[01]+', binary_string):
        if t.lower().startswith('0b'):
            t = t[2:]
        v = int(t, 2)
        if 0 <= v <= 255:
            vals.append(v)
    return _decode(vals)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="convert binary to text. ex: \"0b1110000 1101001\" or \"1110000 1101001\"")
    parser.add_argument('-s', '--string', type=str, metavar="string", help='binary numbers separated by spaces. Ex: "1110000 1101001 1100011 1101111" with the quotes')
    parser.add_argument('-f', '--file', type=str, metavar="filename", help='file containing the binary numbers separated by spaces')
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

    print(bin_to_text(data))
