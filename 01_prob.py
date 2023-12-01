# PART 1:
# 1. Find first and last number in each row.
# 2. Put those two digits together to form one number (1, 5 = 15)
# 3. Sum those two digit numbers for each row.


input_data = open('01_input.txt', 'r').readlines()

two_dig_list = []
for i in input_data:
    extract_numbers = [char for char in i if char.isdigit()]
    two_dig_list.append(int(extract_numbers[0] + extract_numbers[-1]))

print(f"Total two dig numbers for part 1: {sum(two_dig_list)}")

# PART 2: 
# 1. Now find the numbers written AS WORDS in each line and also the digits.
# PROBLEM - words overlap (e.g,. eightwo), need to replace from left to right -> 8wo, not eigh2. :-(
# 2. Find first and last number, reguardless of format.
# 3. Sum two dig numbers in the list.

number_words = {
    "zero": "z0o",
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e"
}

# Since some words overlap (eightwo), we need to do some weird stuff to replace the word with an int but still keep the first and last letters of the word
# in case they're part of another number-word.

two_dig_list = []
for i in input_data:    
    for w in number_words.keys():
        i = i.replace(w, number_words[w])

    extract_numbers = [char for char in i if char.isdigit()]
    two_dig_list.append(int(extract_numbers[0] + extract_numbers[-1]))

print(f"Total two dig numbers for part 2: {sum(two_dig_list)}")