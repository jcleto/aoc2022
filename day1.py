results = []
cal = 0

with open('input1.txt') as f:
    for line in f:
        if not line.rstrip('\n'):
            results.append(cal)
            cal = 0
            continue
        cal += int(line.rstrip('\n'))
    results.append(cal)

results.sort()
# a
print(results[-1])
# b
print(sum(results[-3:]))
