#!/usr/bin/env python3
from math import floor
from sys import argv, exit, stderr
from typing import MutableSequence

class IntcodeMachine:
	"""Intcode VM"""
	memory: MutableSequence
	instruction_pointer: int
	running: bool

	def __init__(self, memory: MutableSequence) -> None:
		self.memory = memory
		self.instruction_pointer = 0
		self.running = False
		self.opcodes = {}
	
	def add(self) -> None:
		memory = self.memory
		instruction_pointer = self.instruction_pointer

		left_input = memory[instruction_pointer + 1]
		right_input = memory[instruction_pointer + 2]
		output = memory[instruction_pointer + 3]

		# print(f'add: {left_input}, {right_input}, {output}')
		memory[output] = memory[left_input] + memory[right_input]
		self.instruction_pointer += 3

	def multiply(self) -> None:
		memory = self.memory
		instruction_pointer = self.instruction_pointer

		left_input = memory[instruction_pointer + 1]
		right_input = memory[instruction_pointer + 2]
		output = memory[instruction_pointer + 3]

		# print(f'multiply: {left_input}, {right_input}, {output}')
		memory[output] = memory[left_input] * memory[right_input]
		self.instruction_pointer += 3

	def halt(self) -> None:
		# print('halt')
		self.running = False

	def run(self) -> int:
		memory = self.memory
		opcodes = self.opcodes

		opcodes[1] = self.add
		opcodes[2] = self.multiply
		opcodes[99] = self.halt

		self.running = True
		while self.running:
			# print(f'instruction_pointer: {self.instruction_pointer}')
			# print(f'opcode: {memory[self.instruction_pointer]}')
			# print(f'memory: {memory}')
			self.opcodes[memory[self.instruction_pointer]]()
			self.instruction_pointer += 1
		return memory[0]

def main():
	if len(argv) != 2:
		print(f'Usage: {argv[0]} file_name', file=stderr)
		return 2
	else:
		with open(argv[1], 'r') as memory_file:
			memory = [int(n) for n in memory_file.read().split(',')]
			vm = IntcodeMachine(memory)
			print(vm.run())
		return

if __name__ == '__main__':
	exit(main())
