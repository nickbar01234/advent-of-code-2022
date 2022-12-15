#!/usr/bin/python3
import sys
from collections import deque
import re

def create(data):
	stack = [deque([]) for i in range(9)]
	idx = 0
	while True:
		line = data[idx]
		pos = 0
		for i in range(1, len(line), 4):
			if line[i] == '1':
				return (data[idx + 2:], stack)
			elif line[i] != " ":
				stack[pos].append(line[i])
			pos += 1
		idx += 1

def a(data):
    rest, stack = create(data)
    for line in rest:
        count, start, end = (map(int, re.findall("\d+", line)))
        for _ in range(count):
            stack[end - 1].appendleft(stack[start - 1].popleft())
    top = "".join([x[0] for x in stack])
    print(f"Part A solution {top}")

def b(data):
    rest, stack = create(data)
    for line in rest:
        count, start, end = (map(int, re.findall("\d+", line)))
        crates = [stack[start - 1].popleft() for _ in range(count)]
        for _ in range(count):
            stack[end - 1].appendleft(crates.pop())
    top = "".join([x[0] for x in stack])
    print(f"Part B solution {top}")

if __name__ == "__main__":
    data = [line for line in sys.stdin]
    a(data)
    b(data)
