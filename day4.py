#!/usr/bin/python3
import sys

def parse(line):
	return \
		list(map(lambda x: list(map(int, x.split("-"))) ,
		line.strip().split(",")))

def a(data):
	contained = 0
	overlap = lambda l, r: l[0] <= r[0] and r[1] <= l[1]
	for line in data:
		p1, p2 = parse(line)
		if overlap(p1, p2) or overlap(p2, p1): 
			contained += 1
	print(f"Part A solution {contained}")

def b(data):
	pairs = 0
	overlap = lambda l, r: l[0] <= r[0] and r[0] <= l[1]
	for line in data:
		p1, p2 = parse(line)
		if overlap(p1, p2) or overlap(p2, p1):
			pairs += 1
	print(f"Part B solution {pairs}")

if __name__ == "__main__":
	data = [line for line in sys.stdin]
	a(data)
	b(data)
