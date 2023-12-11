# Oh god. Parsing this input.... sad.

# PRE-WORK: Read in the input and parse out the parts we need to do the rest.

#Each line within a map contains three numbers: the destination range start, 
# the source range start, and the range length.

from multiprocessing import Pool


raw_data = [line.strip() for line in open('05_input.txt', 'r')]

list_of_maps = ["seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light", 
                "light-to-temperature", "temperature-to-humidity", "humidity-to-location"]

dest_source_maps = [[] for i in range(len(list_of_maps))]

current_map_index = -1
map_name = ''

for line in raw_data:
    if line == '':
        continue

    if "seeds" in line:
        seeds = [int(s) for s in line.split(':')[1].strip().split()]
        continue

    if any(char.isalpha() for char in line): # This is a dictionary header.
        map_name = line.split()[0]
        current_map_index = list_of_maps.index(map_name)
    else:
        map_values = tuple([int(v) for v in line.split()])
        dest_source_maps[current_map_index].append(map_values)



def get_map_value(value, dest_source_map):
    map_output = value
    for d, s, r in dest_source_map:
        if value >= s and value < (s + r):
            diff = value - s
            map_output = d + diff
    
    return map_output
    

def get_seed_location(seed, dest_source_maps):
    next_val = seed
    for m in dest_source_maps:
        next_val = get_map_value(next_val, m)

    return next_val


print(f"Part 1: Lowest location is: {min([get_seed_location(s, dest_source_maps) for s in seeds])}")

# Part 2: Seed list is actually pairs, with a seed number followed by range after that. Ex 4, 2 would be 4, 5
# Now find min location for this set of seeds.

# Now we need be efficient again. Here's one example from the input (value, range) = 3169137700 271717609
def get_min_seed_locations_per_pair(pair, dest_source_maps):
    min_seed_location = 1e12
    s_min, s_max = pair
    for s in range(s_min, s_max+1):
        seed_loc = get_seed_location(s, dest_source_maps)
        if seed_loc < min_seed_location:
            min_seed_location = seed_loc
    
    return min_seed_location


def p2():
    p2_seeds_min_max = []
    for i, s in enumerate(seeds):
        if i % 2 == 0:
            start = s
            seed_range = seeds[i+1]
            p2_seeds_min_max.append((s, start+seed_range-1))

    # Create a Pool of worker processes
    pool = Pool()
    min_per_pair = []
    processes = []
    for pair in p2_seeds_min_max:
        processes.append(pool.apply_async(get_min_seed_locations_per_pair, (pair, dest_source_maps)))
    
    print(processes)
    print(processes[0].get())
    for process in processes:
        min_per_pair.append(process.get())
    
    return min(min_per_pair)


if __name__ == '__main__':
    print(f"Part 2: {p2()}")
