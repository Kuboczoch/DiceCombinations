import sys
from DiceCombinations.Dices import Dices

dice = Dices(1, 4, 3)
dice.print_array(None, dice.bigger_than(0, 9, dice.array_sum()))

print("\nEND")
