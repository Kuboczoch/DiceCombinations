class Dices:

    def __init__(self, default_value, max_on_dice, number_of_dices):
        self.array = []
        self.default_value = default_value
        self.max_on_dice = max_on_dice
        self.number_of_dices = number_of_dices

    def increment_array(self, my_list, element=None):
        if element is None:
            element = len(my_list) - 1
        if (my_list[element] + 1) > self.max_on_dice:
            my_list[element] = self.default_value
            if element - 1 < 0:
                return my_list
            my_list = self.increment_array(my_list, element - 1)
        else:
            my_list[element] += 1
        return my_list

    def generate_full_combinations(self):
        max_combinations = self.max_on_dice ** self.number_of_dices
        default_array = []
        while len(default_array) < self.number_of_dices:
            default_array.append(self.default_value)
        while len(self.array) < max_combinations:
            self.array.append(default_array.copy())
            default_array = self.increment_array(default_array, 1)
        return self.array
