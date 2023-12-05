# PART 1: Find match between lotto numbers and lotto cards.
# "Figure out which of the numbers you have appear in the list of winning numbers. 
# The first match makes the card worth one point and each match after the first doubles the point value of that card.""

"""
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""

# 1. Parse each card-line into a set of winners and a set of values on the card.
# 2. Find the intersection.
# 3. Find points - doubled for , startig w 1 pt.
# 4. Sum points.

import re

raw_data = [re.sub(r'\s+', ' ', line.strip()) for line in open('04_input.txt', 'r')]

def make_set_from_string(str_input):
    return set([int(n) for n in str_input.strip().split(' ')])    

def calc_card_points(winning_numbers):
    if len(winning_numbers) > 0:
        return 2**(len(winning_numbers)-1)
    else:
        return 0

card_win_dict = {} 
card_pts = []
for line in raw_data:
    cardn_card_vals = line.split(':')
    card_n = int(cardn_card_vals[0].split(' ')[1]) 
    card_vals  = cardn_card_vals[1].split('|')
    winners = make_set_from_string(card_vals[0])
    card_nums = make_set_from_string(card_vals[1])
    winning_nums = winners.intersection(card_nums)
    card_pts.append(calc_card_points(winning_nums))
    card_win_dict[card_n] = winning_nums

print(f"Part 1: Total card points is {sum(card_pts)}") # 28538

# PART 2: Number of winners is actually number, consecutively from the current card that you get copies of.
# Ex: Card 1 has 4 winners -> get copies of cards 2, 3, 4, 5. 
# Find total number of cards you have, including the originals, following this new rule.

# See if we can do this inefficiently
cards = len(card_win_dict.keys())
max_card_val = max(card_win_dict.keys())

cards_to_draw = {}
cards_remaining = {}

for c, w in card_win_dict.items():
    wins = card_win_dict[c]
    highest_new_card = min(max_card_val, c + len(wins))
    new_cards = list(range(c + 1, highest_new_card + 1))
    cards_to_draw[c] = new_cards
    cards_remaining[c] = 1

for c in sorted(cards_remaining.keys()):
    print(f"Card: {c}")
    num_of_times_to_add = cards_remaining[c]
    cards_to_add = cards_to_draw[c]
    cards += len(cards_to_add) * num_of_times_to_add
    cards_remaining[c] -= num_of_times_to_add
    for new_c in cards_to_add:
        cards_remaining[new_c] += num_of_times_to_add


print(f"Part 2: Total lotto cards are now {cards}")
