# PROBLEM 7: Card games

raw_data = [line.strip().split() for line in open('tmp.txt', 'r').readlines()]

card_map = {"A":"M", "K":"L", "Q":"K", "J":"J", "T":"I", "9":"H", "8":"G", "7":"F", 
            "6":"E", "5":"D", "4":"C", "3":"B", "2":"A"}

# Hand order: five, four, full house, three, two pair, one pair, high_card -> 7,6,5,4,3,2,1


def get_hand_type(collected_values):
    if len(collected_values) == 1:
        hand_type = 7
    elif collected_values[0][1] == 4:
        hand_type = 6
    elif collected_values[0][1] == 3:
        if len(collected_values) == 2:
            hand_type = 5
        else:
            hand_type = 4
    elif collected_values[0][1] == 2:
        if collected_values[1][1] == 2:
            hand_type = 3
        else:
            hand_type = 2
    else:
        hand_type = 1

    return hand_type


def parse_cards(hand):
    sorted_hand = sorted(hand)
    card_to_count = []
    for c in sorted_hand:
        ct_n = sorted_hand.count(c)
        card_to_count.append((c, ct_n))
    
    unique_card_ct = list(set(card_to_count))
    collected_values = sorted(unique_card_ct, key=lambda x: x[1], reverse=True)

    return get_hand_type(collected_values)


hand_bid = {}
hand_to_type = []

def get_points(raw_data, card_map, use_joker = False):
    for h, b in raw_data:
        new_hand = ''.join([card_map[v] for v in list(h)])
        hand_bid[new_hand] = int(b)

        if use_joker:


        else:
            hand_type = parse_cards(new_hand)
        
        hand_to_type.append((new_hand, hand_type))

    order_hands = sorted(hand_to_type, key=lambda x: (x[1], x[0]))

    total_points = 0
    for i, h in enumerate(order_hands):
        bid = hand_bid[h[0]]
        total_points += (i+1) * bid

    return total_points

print(f"Part 1:\n{get_points(raw_data, use_joker=False)}") 

# PART 2: J cards are now jokers (wildcards), use in the most advantagous way possible.
card_map_joker = {"A":"M", "K":"L", "Q":"K", "J":"A", "T":"J", "9":"I", "8":"H", "7":"G", 
            "6":"F", "5":"E", "4":"D", "3":"C", "2":"B"}

