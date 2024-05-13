from functools import cache
from math import comb

sent = input()
received = input()


@cache
def command_to_position(command):
    position = 0
    for i in range(len(command)):
        if command[i] == "+":
            position += 1
        elif command[i] == "-":
            position -= 1
    return position

# combinations???
def calculate_probability(desired_position, actual_position, confusions):
    diff = abs(desired_position - actual_position)
    if diff > confusions:  # can't reach it monotonically
        return 0
    possible_combinations = comb(confusions, (confusions + diff) // 2)
    return possible_combinations * (0.5**confusions)


probability = calculate_probability(
    command_to_position(sent), 
    command_to_position(received), 
    received.count("?")
)
print("{0:.12f}".format(probability))
