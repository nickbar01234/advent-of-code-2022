#!/usr/bin/python3
import sys

class Folder:
    def __init__(self, name, parent = None):
        self.name = name
        self.parent = parent
        self.dir = {}
        self.size = 0

    def extend(self, name):
        if name not in self.dir:
            child = Folder(name)
            self.dir[name] = child
            child.parent = self
        return self

    def get(self, name):
        return self.dir[name]

def build(data):
    head = p = Folder('/')
    idx = 0
    while idx < len(data):
        command = data[idx].strip().split(" ")[1]
        if command == "ls":
            idx += 1
            while idx < len(data) and data[idx][0] != "$":
                first, second = data[idx].strip().split(" ")
                if first.isnumeric():
                    p.size += int(first)
                else:
                    p.extend(second)
                idx += 1
        else:
            directory = data[idx].strip().split(" ")[-1]
            if directory == "/":
                while p.parent != None:
                    p = p.parent
            elif directory == "..":
                p = p.parent
            else:
                p = p.get(directory)
            idx += 1
    return head

def sizeof(folder):
    for child in folder.dir.values():
        folder.size += sizeof(child)
    return folder.size

def a(folder):
    solution = 0
    def traverse(p: Folder):
        nonlocal solution
        size = p.size
        if p.size <= 100000:
            solution += size
        for child in p.dir.values():
            size += traverse(child)
        return size

    traverse(folder) 
    print(f"Part A solution {solution}")

def b(folder):
    required = 30000000 - (70000000 - folder.size) 
    solution = float("inf")    
    def min(p):
        nonlocal solution, required
        if p.size >= required and p.size < solution:
            solution = p.size
        for child in p.dir.values():
            min(child)
    min(folder)
    print(f"Part B solution {solution}")

if __name__ == "__main__":
    data = [line for line in sys.stdin]
    directory = build(data)
    sizeof(directory)
    a(directory)
    b(directory)