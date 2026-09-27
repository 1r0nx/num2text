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


def ascii_to_text(s):
    """Convert decimal byte values (any separator) to text. Tokens outside the
    byte range 0-255 are skipped so noisy input never crashes the tool."""
    vals = []
    for code in re.findall(r'\d+', s):
        v = int(code)
        if 0 <= v <= 255:
            vals.append(v)
    return _decode(vals)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="convert ascii (decimal) to text. ex: \"72 101 108 108 111\"")
    parser.add_argument('-s', '--string', type=str, metavar="string", help='ascii numbers separated by spaces. Ex: "72 101 108 108 111" with the quotes')
    parser.add_argument('-f', '--file', type=str, metavar="filename", help='file containing the ascii numbers separated by spaces')
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

    print(ascii_to_text(data))
