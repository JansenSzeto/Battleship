'''
██████╗░░█████╗░████████╗████████╗██╗░░░░░███████╗  ░██████╗██╗░░██╗██╗██████╗░
██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║░░░░░██╔════╝  ██╔════╝██║░░██║██║██╔══██╗
██████╦╝███████║░░░██║░░░░░░██║░░░██║░░░░░█████╗░░  ╚█████╗░███████║██║██████╔╝
██╔══██╗██╔══██║░░░██║░░░░░░██║░░░██║░░░░░██╔══╝░░  ░╚═══██╗██╔══██║██║██╔═══╝░
██████╦╝██║░░██║░░░██║░░░░░░██║░░░███████╗███████╗  ██████╔╝██║░░██║██║██║░░░░░
╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚══════╝╚══════╝  ╚═════╝░╚═╝░░╚═╝╚═╝╚═╝░░░░░
'''
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
total = 5
def distance():
    pass

# ⚓ 
def carrier():
    direction = random.randrange(0, 4)
    t = random.randrange(0, 6)
    u = random.randrange(0,10)
    global answer
    if direction == 0:
        for k in range(5):
            answer.append([u, t+k])
    elif direction == 1:
        for k in range(5):
            answer.append([t+k, u])
    elif direction == 2:
        t = random.randrange(5, 11)
        for k in range(5):
            answer.append([u, t-k])
    elif direction == 3:
        t = random.randrange(5, 11)
        for k in range(5):
            answer.append([t-k, u])

def start():
    carrier()
    show()
def win():
    os.system('cls')
    won = open("won.txt", "r", encoding="utf-8")
    print(won.read())
    time.sleep(3)
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
    title = open("title.txt", "r", encoding="utf-8")
    print(title.read())
    print(got)
    global message
    for i in message:
        print(i)
    for a in grid:
        print(" ".join(a))
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
    try:
        ans_list = []
        ans_list.append(x)
        ans_list.append(y)
        check(ans_list)
    except IndexError:
        message.clear()
        message.append("Out of range!")
        show()
if __name__ == '__main__':
    start()