with open('input_adv2.txt') as f:
    list = [line.rstrip() for line in f]

def splitter(str):
    chunks = str.split(' ')
    return chunks

x = 0
y = 0
aim = 0


def position(item):
    global x, y, aim
    if splitter(item)[0] == 'forward':
        x += int(splitter(item)[1])
        aim += y * int(splitter(item)[1])

    elif splitter(item)[0] == 'up':
        y -= int(splitter(item)[1])

    elif splitter(item)[0] == 'down':
        y += int(splitter(item)[1])


for item in list:
    position(item)

print(x*y)
print(x*aim)
