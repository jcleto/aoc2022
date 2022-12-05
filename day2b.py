move = None
points = 0
opponent = {"A": "Rock", "B": "Paper", "C": "Scissors"}
me = {"X": "lose", "Y": "draw", "Z": "win"}
items = {"Rock": 1, "Paper": 2, "Scissors": 3}

with open('input2.txt') as f:

    for line in f:
        p1 = line[0]
        p2 = line[2]

        if me[p2] == "draw":
            move = opponent[p1]

        if me[p2] == "win":
            if opponent[p1] == "Rock":
                move = "Paper"

            if opponent[p1] == "Paper":
                move = "Scissors"

            if opponent[p1] == "Scissors":
                move = "Rock"

        if me[p2] == "lose":
            if opponent[p1] == "Rock":
                move = "Scissors"

            if opponent[p1] == "Paper":
                move = "Rock"

            if opponent[p1] == "Scissors":
                move = "Paper"

        if me[p2] == "draw":
            points += 3

        if me[p2] == "win":
            points += 6

        points += items[move]

print(points)
