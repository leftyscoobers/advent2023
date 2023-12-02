# PART 1: Ball limits = 12 red, 13 green, 14 blue
# 1. Parse input to record something like game num, n red, n blue, n green
# 2. For each game, determine if possible given limits. If so, record game number
# 3. Sum game numbers that are possible.

import numpy as np

raw_data = open('02_input.txt', 'r').readlines()


def parse_line(line):
    game, balls = line.strip().split(':')
    game_num = int(game.split(' ')[1])
    ball_draws = balls.split(';')

    ct_by_color = {
        "red": [],
        "green": [],
        "blue": []
    }

    for draw in ball_draws:
        color_cts = [i.strip() for i in draw.split(',')]
        for ct_pair in color_cts:
            ct, col = ct_pair.split()
            ct_by_color[col].append(int(ct)) 
        
    # Find max for each color and return name num + max in [red, green, blue]
    color_max = [max(ct_by_color[color]) for color in ['red', 'green', 'blue']]

    return game_num, color_max

max_possible = np.array([12, 13, 14])
possible_game_nums = []
for game in raw_data:
    game_n, color_max = parse_line(game)
    print(color_max)
    compare = max_possible - color_max
    print(compare)
    if all(compare >= 0):
        print(game_n)
        possible_game_nums.append(game_n)

print(f"Part 1: Sum of possible games is {sum(possible_game_nums)}")
