import sys
from DiceCombinations.Dices import Dices

dice1 = Dices(1, 6, 8)
my_array = dice1.generate_full_combinations()
dice1.print_array()
print("END")
