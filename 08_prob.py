# PROBLEM 8: Search a map

# PART 1: Use the mappings in the input to figure out the path from AAA to ZZZ using the "turns" in line one.
# How many steps are required to get to ZZZ?

"""
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
"""

from math import lcm

turns = []
node_map = {}

for line in open('08_input.txt', 'r'):
    l = line.strip()
    if turns == []:
        turns = list(l)
    elif l == '':
        continue
    else:
        split = [p.strip() for p in l.split('=')]
        dict_key = split[0]
        matchtups = [m.strip() for m in split[1].replace('(', '').replace(')', '').split(',')]
        node_map[dict_key] = matchtups


def get_new_loc(current, turn, nodes):
    if turn == 'L':
        new_loc = nodes[current][0]
    else:
        new_loc = nodes[current][1]
    return new_loc


steps = 0
curr_location = 'AAA'

at_zzz = False
while not at_zzz:
    for t in turns:
        new_location = get_new_loc(curr_location, t, node_map)
        steps += 1

        if new_location == 'ZZZ':
            at_zzz = True
            break
        else:
            curr_location = new_location
            
print(f"Part 1: Steps to get to ZZZ = {steps}")

# PART 2: Simultaneous paths
# Now start at multiple nodes - all ending with A, follow all paths from all of those nodes.
# We need to know when all of them will hit a node ending in Z on the same step.
# But we DON'T need to follow each path until we get to this point - they will repeat.
# Stop each path once we hit a z node and record the step at which that happens. 
# When all paths to (all) the z nodes are found, stop and find the least common multiple of those paths - 
# thats where all paths hit a z node on the same step. 

start_nodes = [n for n in node_map.keys() if n[2] == 'A']

steps_per_node = []
curr_nodes = start_nodes


for n in curr_nodes:
    steps = 0
    step_node = n
    step_node_has_z = False
    
    while not step_node_has_z:
        for t in turns:
            new_node = get_new_loc(step_node, t, node_map)
            steps += 1

            if new_node[2] == 'Z':
                step_node_has_z = True
                steps_per_node.append(steps)
                break
            else:
                step_node = new_node

print(f"Part 2: Steps to get to all Z-ending nodes {math.lcm(*steps_per_node)}")

# Likely problem - multiple ways to terminate at Z but I'm stopping at the first one. Try it first.
