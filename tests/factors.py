#!/usr/bin/python3
from sys import argv

def factorize(number):
	factor = []
	for a in range(2, int(number ** 0.5) + 1):
		while number % a == 0:
			factor.append(a)
			number //= a
	
	if number > 1:
		factor.append(number)
	return (factor)

def file_factorize(file):
	with open(file, 'r') as file:
		for row in file:
			num = int(row)
			factor = factorize(num)
			p = factor[0]
			q = num // p
			print("{}={}*{}".format(num, p, q))

if __name__ == '__main__':
	if len(argv) < 2:
		print("Usage: factors <file>")
		sys.exit(1)

	file = argv[1]
	file_factorize(file)
