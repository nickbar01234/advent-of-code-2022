#!/usr/bin/python3
import sys

if __name__ == "__main__":
	calories = []
	tmp = 0
	for line in sys.stdin:
		data = line.strip()
		if data == "":
			calories.append(tmp)
			tmp = 0
		else:
			tmp += int(data)
	
	calories = sorted(calories)
	print(f"Part A solution {max(calories)}")
	print(f"Part B solution {sum(calories[-3:])}")
