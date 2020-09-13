import os
import random
import time
import sys
grid = [
    ["○", "○", "○", "○", "○", "○", "○", "○", "○", "○"],
    ["○", "○", "○", "○", "○", "○", "○", "○", "○", "○"],
    ["○", "○", "○", "○", "○", "○", "○", "○", "○", "○"],
    ["○", "○", "○", "○", "○", "○", "○", "○", "○", "○"],
    ["○", "○", "○", "○", "○", "○", "○", "○", "○", "○"],
    ["○", "○", "○", "○", "○", "○", "○", "○", "○", "○"],
    ["○", "○", "○", "○", "○", "○", "○", "○", "○", "○"],
    ["○", "○", "○", "○", "○", "○", "○", "○", "○", "○"],
    ["○", "○", "○", "○", "○", "○", "○", "○", "○", "○"],
    ["○", "○", "○", "○", "○", "○", "○", "○", "○", "○"],
]
answer = []
message = []
got = 0
total = 17
a = 0
def distance():
    pass

# ⚓ 
def ship():
    global answer
    global a
    direction = random.randrange(0, 4)
    u = random.randrange(0, 10)
    k = (5, 4, 3, 3, 2)
    test = []
    ok = True
    if direction == 0:
        t = random.randrange(0, 11-k[a])
        for x in range(k[a]):
            test.append([t+x, u])
    elif direction == 1:
        t = random.randrange(0, 11-k[a])
        for x in range(k[a]):
            test.append([u, t+x])
    elif direction == 2:
        t = random.randrange(9-k[a], 10)
        for x in range(k[a]):
            test.append([t-x, u])
    elif direction == 3:
        t = random.randrange(9-k[a], 10)
        for x in range(k[a]):
            test.append([u, t-x])
    for x in test:
        if x in answer:
            ok = False
        else:
            pass
    if ok == True:
        for z in test:
            answer.append(z)
        if a == 4:
            pass
        else:
            a += 1
            ship()
    else:
        ship()
            

def start():
    global answer
    answer.clear()
    ship()
    # for x in answer:
        # grid[x[1]][x[0]] = "⨂"
    show()
def win():
    os.system('cls')
    # won = open("won.txt", "r", encoding="utf-8")
    # print(won.read())
    print("-----You Won!-----")
    input()
    sys.exit(0)
def check(c):
    message.clear()
    global grid
    global answer
    if c in answer:
        message.append("Hit!")
        grid[c[1]][c[0]] = "✓"
        global got
        got += 1
        answer.remove(c)
        pass
    else:
        message.append("Miss!")
        grid[c[1]][c[0]] = "✗"
        pass
    if got == total:
        win()
    show()
def show():
    os.system('cls')
    global grid
    print(answer)
    #title = open("title.txt", "r", encoding="utf-8")
    # print(title.read())
    print("Battleship")
    print(f"""Hit: {got}""")
    global message
    for i in message:
        print(i)
    print("  0 1 2 3 4 5 6 7 8 9")
    k = -1
    for a in grid:
        k += 1
        print(str(k)+" "+str(" ".join(a)))
    input_ = input().split()
    message.clear()
    try:
        x = int(input_[0])
        y = int(input_[1])
        pass
    except ValueError:
        message.clear()
        message.append("Invalid")
        show()
        message.clear()
    except IndexError:
        show()
    try:
        ans_list = []
        ans_list.append(x)
        ans_list.append(y)
        check(ans_list)
    except IndexError:
        message.clear()
        message.append("Out of range!")
        show()

start()