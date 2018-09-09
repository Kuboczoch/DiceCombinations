import sys

dices = 2
max_dots = 6


def number_to_power(number, power):
    power -= 1
    number *= number
    if power != 0:
        number_to_power(number, power)
    return number


max_combinations = number_to_power(max_dots, dices)

combinations = []


def increment_combination(combination=None, element=None):
    if combination is None:
        combination = []
        while len(combination) < dices:
            combination.append(1)
        return combination
    if element is None:
        element = dices - 1


def fill_combination():
    while len(combinations) < max_combinations:
        combinations.append(increment_combination())


fill_combination()

print("END")
