#!/usr/bin/python3
import sys

def a(data):
    line = data[0].strip()
    length = len(line)
    seen = set()

    i = j = 0
    while j < length:
        if len(seen) == 4:
            print(f"Part A solution {j}")
            return
        
        if line[j] in seen:
            seen.discard(line[i])
            i += 1
        else:
            seen.add(line[j])
            j += 1

def b(data):
    line = data[0].strip()
    length = len(line)
    seen = set()

    i = j = 0
    while j < length:
        if len(seen) == 14:
            print(f"Part B solution {j}")
            return
        
        if line[j] in seen:
            seen.discard(line[i])
            i += 1
        else:
            seen.add(line[j])
            j += 1

if __name__ == "__main__":
    data = [line for line in sys.stdin]
    a(data)
    b(data)