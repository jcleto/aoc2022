result = None
points = 0
opponent = {"A": "Rock", "B": "Paper", "C": "Scissors"}
me = {"X": "Rock", "Y": "Paper", "Z": "Scissors"}
items = {"Rock": 1, "Paper": 2, "Scissors": 3}

with open('input2.txt') as f:

    for line in f:
        p1 = line[0]
        p2 = line[2]

        if opponent[p1] == me[p2]:
            result = "draw"

        if opponent[p1] == "Rock" and me[p2] == "Paper":
            result = "win"

        if opponent[p1] == "Rock" and me[p2] == "Scissors":
            result = "loss"

        if opponent[p1] == "Paper" and me[p2] == "Rock":
            result = "loss"

        if opponent[p1] == "Paper" and me[p2] == "Scissors":
            result = "win"

        if opponent[p1] == "Scissors" and me[p2] == "Rock":
            result = "win"

        if opponent[p1] == "Scissors" and me[p2] == "Paper":
            result = "loss"

        if result == "draw":
            points += 3

        if result == "win":
            points += 6

        points += items[me[p2]]

print(points)
