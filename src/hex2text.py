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


def hex_to_text(hex_string):
    """Convert hex byte values (with or without separators or '0x' prefix) to
    text. Each token is 1-2 hex digits (always a valid byte), so odd-length or
    noisy input never crashes the tool."""
    vals = []
    for t in re.findall(r'0x[0-9a-fA-F]{1,2}|[0-9a-fA-F]{2}|[0-9a-fA-F]', hex_string):
        h = t[2:] if t.lower().startswith('0x') else t
        vals.append(int(h, 16))
    return _decode(vals)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="convert hex to text. ex: \"0x48 0x65 0x6C 0x6C 0x6F\" or \"48 65 6C 6C 6F\" or \"48656c6c6f\"")
    parser.add_argument('-s', '--string', type=str, metavar="string", help='hex numbers separated by spaces. ex: "48 65 6C 6C 6F" with the quotes')
    parser.add_argument('-f', '--file', type=str, metavar="filename", help='file containing the hex numbers separated by spaces')
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

    print(hex_to_text(data))
