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

raw_data = [line.strip() for line in open('11_input.txt', 'r').readlines()]
rows = len(raw_data)
cols = len(raw_data[0])

initial_galaxies = []
for i, row in enumerate(raw_data):
    if '#' in row:
        for pos, g in enumerate(row):
            if g == '#':
                initial_galaxies.append((i, pos))

# Use galaxies to find empty cols/rows next
initial_empty_rows = [i for i in range(rows) if i not in [coord[0] for coord in initial_galaxies]]
initial_empty_cols = [i for i in range(cols) if i not in [coord[1] for coord in initial_galaxies]]

# Expand universe by doubling the empty row and col space. Kind of annoying. Actually we could skip this -
# we can add to coordinates while we find distance instead.
def expand_universe(galaxies, empty_rows, empty_cols, expand_factor):
    expanded_galaxies = set()
    for row, col in galaxies:
        new_row = row
        new_col = col
        for r in empty_rows:
            if row > r:
                new_row += (expand_factor-1)
        for c in empty_cols:
            if col > c:
                new_col += (expand_factor-1)
        expanded_galaxies.add((new_row, new_col))
    return expanded_galaxies


# Find distance between each (no diagonal)
def get_distance(pair1, pair2):
    row_diff = abs(pair2[0] - pair1[0])
    col_diff = abs(pair2[1] - pair1[1])
    return row_diff + col_diff


def find_total_distances(start_universe, empty_rows, empty_cols, expand_factor):
    used_galaxies = set()
    total_distance = 0
    expanded_galaxies = expand_universe(start_universe, empty_rows, empty_cols, expand_factor)
    for galaxy in expanded_galaxies:
        used_galaxies.add(galaxy)
        pairings = expanded_galaxies.difference(used_galaxies)
        distances = [get_distance(p, galaxy) for p in pairings]
        total_distance += sum(distances)
    
    return total_distance

print(f"Part 1: total distance between pairs is {find_total_distances(initial_galaxies, initial_empty_rows, initial_empty_cols, 2)}")
print(f"Part 2: total distance between pairs is {find_total_distances(initial_galaxies, initial_empty_rows, initial_empty_cols, 1e6)}")

