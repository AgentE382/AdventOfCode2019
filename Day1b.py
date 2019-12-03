#!/usr/bin/env python3
from math import floor
from sys import argv, exit, stderr

def fuel_per_part(mass):
	return floor(int(mass) / 3) - 2

def fuel_per_ship(file_name):
	total_fuel = 0
	with open(file_name, 'r') as rocket_ship:
		for part in rocket_ship:
			total_fuel += fuel_per_part(part)
	return total_fuel

def main():
	if len(argv) != 2:
		print(f'Usage: {argv[0]} file_name', file=stderr)
		return 2
	else:
		print(fuel_per_ship(argv[1]))
		return

if __name__ == '__main__':
	exit(main())
