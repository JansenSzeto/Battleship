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
def random_coordinates():
    for x in range(8):
        global grid
        ran_x = random.randrange(0,10)
        ran_y = random.randrange(0,10)
        ran = []
        ran.append(ran_x)
        ran.append(ran_y)
        answer.append(ran)
        # grid[ran_y][ran_x] = "⨳"

def show():
    os.system('clear')
    global grid
    print(answer)
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
        grid[y][x] = "X"
        show()
    except IndexError:
        message.clear()
        message.append("Out of range!")
        show()
random_coordinates()
show()