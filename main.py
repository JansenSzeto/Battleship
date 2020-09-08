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
def random_coordinates():
    for x in range(8):
        global grid
        ran_x = random.randrange(0,10)
        ran_y = random.randrange(0,10)
        ran = []
        ran.append(ran_x)
        ran.append(ran_y)
        answer.append(ran)
        grid[ran_y][ran_x] = "⨳"

def show():
    os.system('clear')
    print(answer)
    for a in grid:
        print(" ".join(a))
    input_ = input().split()
    x = input(input_[0])
    y = input(input_[1])
random_coordinates()
show()