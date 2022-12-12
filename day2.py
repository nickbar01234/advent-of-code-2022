#!/usr/bin/python3
import sys

suggestionToMove = {
  "X": "A",
  "Y": "B",
  "Z": "C"
}

moveToScore = {
  "A": 1,
  "B": 2,
  "C": 3
}

moveToWin = {
  "A": "B",
  "B": "C",
  "C": "A"
}

moveToLose = {
  "A": "C",
  "B": "A",
  "C": "B"
}

WIN, TIE, LOSS = 6, 3, 0

def a(data):
	scores = 0
	for line in data:
		op, suggestion = line.strip().split(" ")
		move = suggestionToMove[suggestion]
		scores += moveToScore[move]

		if move == op:
			scores += TIE
		elif moveToWin[move] == op:
			scores += WIN

	print(f"Part A solution {scores}")

def b(data):
	scores = 0
	for line in data:
		op, outcome = line.strip().split(" ")
		move = ""
		if outcome == "X":
			move = moveToLose[op]
		elif outcome == "Y":
			scores += TIE
			move = op
		else:
			scores += WIN
			move = moveToWin[op]
		scores += moveToScore[move]
	print(f"Part B solution {scores}")

if __name__ == "__main__":
	data = [line for line in sys.stdin]
	a(data)
	b(data)
