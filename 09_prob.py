# PROBLEM 9: Basically find derivatives until you get to zero, then interpolate back "up" to get next predicted value.

"""
0   3   6   9  12  15  18 <- new prediction
  3   3   3   3   3   3 <- using diff below (15 + 3)
    0   0   0   0   0
"""

# PART 1: Find all new predicted values and add them.
# PART 2: Same thing but extrapolate the past value instead of the future.

raw_data = [line.strip() for line in open('09_input.txt', 'r').readlines()]
records = []
for line in raw_data:
    records.append([int(i) for i in line.split()])

def get_prediction(record, for_future=True):
    zeros = [r == 0 for r in record]
    if for_future:
        step_diffs = [record[-1]]
    else:
        step_diffs = [record[0]]

    while not all(zeros):
        diff = [record[i+1] - record[i] for i in range(len(record)-1)]

        if for_future:
            step_diffs.append(diff[-1])
        else:
            step_diffs.append(diff[0])

        record = diff
        zeros = [r ==0 for r in record]

    if for_future:
        return sum(step_diffs)
    else:
        even_idx = sum([s for i, s in enumerate(step_diffs) if i % 2 == 0])
        odd_idx = sum([s for i, s in enumerate(step_diffs) if i % 2 == 1])
        return even_idx - odd_idx

print(f"Part 1: Sum of predictions is {sum([get_prediction(r) for r in records])}")
print(f"Part 2: Sum of extrapolated past values is {sum([get_prediction(r, for_future=False) for r in records])}")

