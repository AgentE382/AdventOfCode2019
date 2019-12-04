#!/usr/bin/env python3
from sys import argv
from re import search


def check_number(s: str) -> bool:
    duplicate_found = False
    previous = s[0]
    for current in s[1:]:
        if current < previous:
            return False
        if current == previous:
            duplicate_found = True
        previous = current
    return duplicate_found


def main():
    if len(argv) != 3:
        print(f'Usage: {argv[0]} <startvalue> <endvalue>', file=stderr)
        return 2
    else:
        print(len([item for item in range(int(argv[1]), int(argv[2])) if check_number(str(item))]))
        return


if __name__ == '__main__':
    exit(main())
