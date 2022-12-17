#!/usr/bin/python3
import sys

def build(data):
    matrix = []
    for line in data:
        heights = [int(h) for h in line.strip()]
        matrix.append(heights)
    return matrix

def a(matrix):
    height, width = len(matrix), len(matrix[0])
    trees = 0
    for i, row in enumerate(matrix):
        for j, h in enumerate(row):
            up = [matrix[idx][j] for idx in range(i)]
            down = [matrix[idx][j] for idx in range(i + 1, height)]
            left = [matrix[i][idx] for idx in range(j)]
            right = [matrix[i][idx] for idx in range(j + 1, width)]
            for rem in [up, down, left, right]:
                if all(map(lambda x: h > x, rem)):
                    trees += 1
                    break

    print(f"Part A solution {trees}")

def b(matrix):
    height, width = len(matrix), len(matrix[0])
    maximum = 0

    def calculate(height, rest):
        count = 0
        for other in rest:
            count += 1
            if other >= height:
                break
        return count

    for i, row in enumerate(matrix):
        for j, h in enumerate(row):
            up = [matrix[idx][j] for idx in reversed(range(i))]
            down = [matrix[idx][j] for idx in range(i + 1, height)]
            left = [matrix[i][idx] for idx in reversed(range(j))]
            right = [matrix[i][idx] for idx in range(j + 1, width)]
            score = 1
            for rest in [up, down, left, right]:
                score *= calculate(h, rest)
            maximum = max(maximum, score)

    print(f"Part B solution {maximum}")

if __name__ == "__main__":
    data = [line for line in sys.stdin]
    matrix = build(data)
    a(matrix)
    b(matrix)