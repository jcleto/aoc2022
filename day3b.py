def get_priority(value):
    r = ord(value) - 96
    if r < 0:
        r = ord(value) - 38
    return r


prio = []
input_file = open('input3.txt')
content_list = input_file.readlines()

for line in input_file:
    total_size = len(line.rstrip('\n'))
    c1 = line[:int(total_size / 2)]
    c2 = line.rstrip('\n')[int(total_size / 2):]

    for char in c1:
        if char in c2:
            common = char
            continue

    prio.append(get_priority(common))

print(sum(prio))
