#!/usr/bin/env python3
from math import floor
from sys import argv, exit, stderr

def fuel_by_mass(mass):
	return floor(int(mass) / 3) - 2

def fuel_per_part(mass):
	total_fuel = 0
	while True:
		partial_fuel = fuel_by_mass(mass)
		if partial_fuel > 0:
			mass = partial_fuel
			total_fuel += partial_fuel
		else:
			return total_fuel

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
