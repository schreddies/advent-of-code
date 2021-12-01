with open('input.txt') as f:
    list = [line.rstrip() for line in f]
    strlist = [int(x) for x in list]

inc = 0

def isIncreasing(i, j):
    global inc
    if j > i:
        inc += 1
    return inc

def firstStar(list):
    for x,y in zip(list[::],list[1::]): 
        inc = isIncreasing(x, y)
    print(inc)

def secStar(list):
    res = [a + b + c for a, b, c in zip(list, list[2:], list[1:])]
    for x,y in zip(res[::],res[1::]): 
        isIncreasing(x, y)
    print(inc)

#firstStar(strlist)
secStar(strlist)
