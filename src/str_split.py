#!/usr/bin/python3

import argparse


def split_string(string, size, sep=" "):
    """Split a string into fixed-size chunks joined by a separator."""
    return sep.join(string[i:i + size] for i in range(0, len(string), size))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="split a string into fixed-size chunks joined by a separator. ex: -s 48656c6c6f -n 2 -> \"48 65 6c 6c 6f\"")
    parser.add_argument('-s', '--string', type=str, metavar="string", required=True, help='string to split. ex: "48656c6c6f"')
    parser.add_argument('-n', '--size', type=int, metavar="size", required=True, help='chunk size (number of characters per group). ex: 2')
    parser.add_argument('-se', '--separator', type=str, metavar="sep", default=" ", help='separator inserted between chunks (default: a space)')
    args = parser.parse_args()

    if args.size < 1:
        parser.error("size must be >= 1")

    print(split_string(args.string, args.size, args.separator))
