def get_priority(value):
    r = ord(value) - 96
    if r < 0:
        r = ord(value) - 38
    return r


def get_common_value(g1, g2, g3):
    s = set(g1).intersection(g2).intersection(g3)
    return ''.join(s)


prio = []
numeric_prio = []

input_file = open('input3.txt')
content_list = input_file.readlines()

for line in range(0, len(content_list), 3):
    prio.append(get_common_value(content_list[line].rstrip('\n'), content_list[line + 1], content_list[line + 2]))

for element in prio:
    numeric_prio.append(get_priority(element))


print(sum(numeric_prio))
