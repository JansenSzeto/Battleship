import os
import random
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

def start():
    for x in range(8):
        global grid
        ran_x = random.randrange(0,10)
        ran_y = random.randrange(0,10)
        ran = []
        ran.append(ran_x)
        ran.append(ran_y)
        answer.append(ran)
    show()
def win():
    import time
    import sys
    os.system('cls')
    won = open("won.txt", "r", encoding="utf-8")
    print(won.read())
    time.sleep(3)
    sys.exit(0)
def check(c):
    message.clear()
    global grid
    if c in answer:
        message.append("Hit!")
        grid[c[1]][c[0]] = "✓"
        global got
        got += 1
        pass
    else:
        message.append("Miss!")
        grid[c[1]][c[0]] = "✗"
        pass
    if got == 2:
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