input_file = open('input4.txt')
content_list = input_file.readlines()

content_list = [item.strip() for item in content_list]
# print(content_list)


def included_pairs(a1, a2, b1, b2):
    if a1 >= b1 and a2 <= b2:
        return 1
    if b1 >= a1 and b2 <= a2:
        return 1
    return 0


def overlap_pairs(a1, a2, b1, b2):
    if a1 < b1 <= a2:
        return 1
    if a1 <= b2 < a2:
        return 1
    if a1 >= b1 and a2 <= b2:
        return 1
    if a1 <= b1 and a2 >= b2:
        return 1

    return 0


results = []

for item in content_list:
    pairs = item.split(',')
    # print(pairs)

    a1 = int(pairs[0].split('-')[0])
    a2 = int(pairs[0].split('-')[1])
    b1 = int(pairs[1].split('-')[0])
    b2 = int(pairs[1].split('-')[1])

    # results.append(included_pairs(a1, a2, b1, b2))
    results.append(overlap_pairs(a1, a2, b1, b2))

print(sum(results))


