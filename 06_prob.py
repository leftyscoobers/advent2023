# PART 1: Time is total time for race, distance is distance to beat. Holding for 1 second = increase in velocity of 1 m/s.

"""
Time:      7  15   30
Distance:  9  40  200
"""

import re
import numpy as np

raw_data = [re.sub(r'\s+', ' ', line.strip()) for line in open('06_input.txt', 'r')]

times = [int(i) for i in raw_data[0].split(":")[1].strip().split()]
dist_to_beat = [int(i) for i in raw_data[1].split(":")[1].strip().split()]

wins_per_race = []
for t, b in zip(times, dist_to_beat):
    possible_distances = [h * (t - h) for h in range(t)]
    wins = [w for w in possible_distances if w > b]
    wins_per_race.append(len(wins))

print(f"Part 1: Product of wins per race is {np.prod(wins_per_race)}")

# PART 2: Actually ignore the spaces and do the same thing. Seems like another optimization problem. *sob*

time = int(''.join([str(i) for i in times]))
one_distance_to_beat = int(''.join([str(i) for i in dist_to_beat]))

def is_win(hold, time, beat):
    return hold * (time - hold) > beat

# Find peak of parabola and iterate from there so we don't have to try every value
mid_h = int(round(time / 2))
print(f"Mid value is {mid_h}")
winner = is_win(mid_h, time, one_distance_to_beat)

wins = 1

# Count up, then do this again counting down. 
h = mid_h
while winner:
    h += 1
    if is_win(h, time, one_distance_to_beat):
        wins += 1
    else:
        winner = False
        print(f"Stopped counting at {h}")

h = mid_h
winner = True
while winner:
    h -= 1
    if is_win(h, time, one_distance_to_beat):
        wins += 1
    else:
        winner = False
        print(f"Stopped counting at {h}")


print(f"Part 2: Possible options to win {wins}")


