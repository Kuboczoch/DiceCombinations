from Dices import Dices

dice = Dices(1, 6, 4)
x = dice.different_values()
dice.print_array(x, dice.any_is(x, 6))
print("\nEND")
