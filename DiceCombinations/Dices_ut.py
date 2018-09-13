import sys
from DiceCombinations.Dices import Dices

dice = Dices(1, 6, 3)
print("\nUnitTest1\n")
dice.print_array(None, dice.bigger_than(0, 9, dice.array_sum_values()))
print("\nUnitTest2\n")
dice.print_array(None, dice.array_and(dice.equal_to(0, 4), dice.equal_to(0, 6)))
print("\nUnitTest3\n")
dice.print_array(None, dice.array_or(dice.equal_to(0, 4), dice.equal_to(0, 6)))
print("\nUnitTest4\n")
my_if_list = dice.print_array(None, dice.array_or(dice.bigger_than(0, 3, dice.array_sum_values()),
                                                  dice.smaller_than(0, 3, dice.array_sum_values())))
print("\nUnitTest5\n")
my_list = dice.combine_array(None, my_if_list)
dice.print_array(my_list)
print("\nEND")
