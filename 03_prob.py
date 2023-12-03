# PART 1: Search around points in a grid
# 1. Go through grid and find numbers.
# 2. For any number that has an adjacent symbol (that is not .), that's an engine part we record.
# 3. Sum the parts.

"""
Example grid:
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

# Consider:
# The concept of 'adjacent' depends on the length of the number.

# Read the data and pad the grid with extra '.' .
import math

raw_data = [['.'] + list(line.strip()) + ['.'] for line in open('03_input.txt', 'r').readlines()]
row_buffer = ['.'] * len(raw_data[0])
grid = [row_buffer] + raw_data + [row_buffer]
grid_rows = len(grid)
grid_cols = len(grid[0])

symbols = set(["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "=", "+", "/"])

def add_location_to_stars(location, part_num, star_dict):
    if location not in star_dict:
        star_dict[location] = []
    star_dict[location].append(part_num)

# First pass, find numbers with location of first digit.
engine_parts = [] # Save as number, location of first dig
star_locations = {}
for row_index, row in enumerate(grid):
    col_index = 0
    while col_index < len(row):
        if row[col_index].isdigit():
            start_col = col_index
            while row[col_index].isdigit():
                col_index += 1
            end_col = col_index-1

            # Now check for engine part feasibility
            top_row = grid[row_index-1][(start_col-1):(end_col+2)]
            bottom_row = grid[row_index+1][(start_col-1):(end_col+2)]
            left = [row[start_col-1]]
            right = [row[end_col+1]]
            adjacent_values = top_row + bottom_row + left + right

            symbols_in_adjacent_cells = symbols.intersection(adjacent_values)
            if symbols_in_adjacent_cells:
                part_num = int(''.join(row[start_col:(end_col+1)]))
                engine_parts.append(part_num)

                # See if part of gear ration (contains "*"). Just slap this together - messy.
                if "*" in symbols_in_adjacent_cells:
                    print(f"-----\n{top_row}\n{left + row[start_col:(end_col+1)] + right}\n{bottom_row}\n-----")

                    if "*" in left:
                        add_location_to_stars((row_index, start_col-1), part_num, star_locations)
                    if "*" in right:
                        add_location_to_stars((row_index, end_col+1), part_num, star_locations)
                    if "*" in top_row:
                        col_indices = [i_c for i_c, value in enumerate(top_row) if value == "*"]
                        for i in col_indices:
                            add_location_to_stars((row_index-1, start_col-1+i), part_num, star_locations)
                    if "*" in bottom_row:
                        col_indices = [i_c for i_c, value in enumerate(bottom_row) if value == "*"]
                        for i in col_indices:
                            add_location_to_stars((row_index+1, start_col-1+i), part_num, star_locations)                                   
        
        else:
            col_index += 1


print(f"Part 1: Sum of engine part numbers: {sum(engine_parts)}") # 527364

# PART 2: Find gear rations - this is where two part numbers share an adjacent "*"
# 1. Find parts with "*" and record location.
# 2. Find parts that share a "*".
# 3. Multiply these parts with shared "*".
# 4. Sum these products.

# Code from part 1 is modified to achieve step 1.

# Assume for now that each gear only touches two parts
gear_ratios = [math.prod(parts) for gear_loc, parts in star_locations.items() if len(parts) > 1]

print(f"Part 2: Sum of gear ratios is {sum(gear_ratios)}") # 70 035 745 is too low should be 79 026 871
