#!/usr/bin/python3

import sys

def priority(items):
	priority = 0
	for item in items:
		if item.islower():
			priority += ord(item) - ord('a') + 1
		else:
			priority += ord(item) - ord('A') + 27
	return priority

def a(data):
	inter = []

	for line in data:
		items = line.strip()
		mid = int(len(items) / 2)
		sack1, sack2 = items[:mid], items[mid:]
		common = set(sack1) & set(sack2)
		inter.extend(list(common))

	score = priority(inter) 
	print(f"Part A solution: {score}")

def b(data):
	inter = []
	i = 0
	while i < len(data):
		first, second, third = list(
			map(lambda x: set(x.strip()), data[i: i + 3])
		)
		inter.extend(list(first & second & third))
		i += 3
	score = priority(inter)
	print(f"Part B solution: {score}")

if __name__ == "__main__":
	data = [line for line in sys.stdin]
	a(data)
	b(data)

