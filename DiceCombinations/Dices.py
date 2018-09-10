import sys


class Dices:

    def __init__(self, default_value, max_on_dice, number_of_dices):
        self.array = []
        self.default_value = default_value
        self.max_on_dice = max_on_dice
        self.number_of_dices = number_of_dices
        self.generate_full_combinations()

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
            default_array = self.increment_array(default_array)
        return self.array

    def print_array(self, array=None, display_only_if=None):
        if array is None:
            array = self.array
        if display_only_if is None:
            i = 0
            display_only_if = []
            while i < len(array):
                display_only_if.append([True])
                i += 1
        i = 0
        inline = 0
        while i < len(array):
            if inline % self.max_on_dice == 0 and inline != 0:
                if display_only_if[i - 1][0] is True:
                    sys.stdout.write('|')
                    sys.stdout.write('\n')
            if display_only_if[i][0] is True:
                sys.stdout.write('|')
            o = 0
            while o < len(array[i]):
                if display_only_if[i][0] is True:
                    sys.stdout.write(str(array[i][o]))
                    inline += 1
                if o != len(array[i]) - 1:
                    if display_only_if[i][0] is True:
                        sys.stdout.write(',')
                o += 1
            i += 1
        if display_only_if[len(display_only_if) - 1][0] is True:
            sys.stdout.write('|')

    def equal_to(self, element, equal_to):
        my_array = []
        i = 0
        while i < len(self.array):
            if self.array[i][element] == equal_to:
                my_array.append([True])
            else:
                my_array.append([False])
            i += 1
        return my_array

    def bigger_than(self, element, bigger_than, array=None):
        if array is None:
            array = self.array
        my_array = []
        i = 0
        while i < len(array):
            if array[i][element] > bigger_than:
                my_array.append([True])
            else:
                my_array.append([False])
            i += 1
        return my_array

    def array_sum(self):
        my_array = []
        i = 0
        while i < len(self.array):
            amount = [0]
            o = 0
            while o < len(self.array[i]):
                amount[0] += self.array[i][o]
                o += 1
            my_array.append(amount.copy())
            i += 1
        return my_array
