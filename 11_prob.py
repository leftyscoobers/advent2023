# PROBLEM 11: GALAXIES IN A GRID

# . are empty space, # are galaxies
# Rows and cols w/o any galaxies expand twice 

"""
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....

Between galaxy 1 and galaxy 7: 15
Between galaxy 3 and galaxy 6: 17
Between galaxy 8 and galaxy 9: 5

Test p1 374
"""

# Part 1: Find shortest path between each pair of galaxies.
# 1. Expand universe
# 2. Find pairs
# 3. Find path length for each pair (no diagonal)
# 4. Sum paths

raw_data = [line.strip() for line in open('tmp.txt', 'r').readlines()]

initial_galaxies = []
for i, row in enumerate(raw_data):
    if '#' in row:
        for g in enumerate(row):
            if g == '#':
                initial_galaxies.append((i, g))

# Use galaxies to find empty cols/rows next
