import sys


class Dices:

    def __init__(self, default_value, max_on_dice, number_of_dices):
        self.array = []
        self.default_value = default_value
        self.max_on_dice = max_on_dice
        self.number_of_dices = number_of_dices
        self.generate_full_combinations()

    def increment_array(self, my_list: list, element: int = None) -> list:
        """
        :param my_list: array[array] [[1, 1] , [1, 1]]
        :param element: array[element from where to increment]
        """
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

    def generate_full_combinations(self) -> list:
        max_combinations = self.max_on_dice ** self.number_of_dices
        default_array = []
        while len(default_array) < self.number_of_dices:
            default_array.append(self.default_value)
        while len(self.array) < max_combinations:
            self.array.append(default_array.copy())
            default_array = self.increment_array(default_array)
        return self.array  # Return array multiple values in array

    def print_array(self, array: list = None, only_if: list = None):
        #  only for debug and terminal view
        #  use combine instead
        """
        :param only_if: list of bools [[True], [False]]
        :param array: list of values [[1, 2], [2, 1]]
        """
        array = self.inherit_array_if_none(array)
        if only_if is None:
            i = 0
            only_if = []
            while i < len(array):
                only_if.append([True])
                i += 1
        i = 0
        inline = 0
        while i < len(array):
            if inline % self.max_on_dice == 0 and inline != 0:
                inline = 0
                sys.stdout.write('|')
                sys.stdout.write('\n')
            if only_if[i][0]:
                sys.stdout.write('|')
            o = 0
            while o < len(array[i]):
                if only_if[i][0]:
                    sys.stdout.write(str(array[i][o]))
                    if o == 0:
                        inline += 1
                if o != len(array[i]) - 1:
                    if only_if[i][0]:
                        sys.stdout.write(',')
                o += 1
            i += 1
        if only_if[len(only_if) - 1][0]:
            sys.stdout.write('|')

    def combine_array(self, array: list = None, only_if: list = None) -> list:
        array = self.inherit_array_if_none(array)
        if only_if is None:
            i = 0
            only_if = []
            while i < len(array):
                only_if.append([True])
                i += 1
        new_array = []
        i = 0
        while i < len(array):
            if only_if[i][0]:
                new_array.append(array[i].copy())
            i += 1
        return new_array

    #  Operations on arrays

    def equal_to(self, element: int, equal_to: int, array: list = None) -> list:
        array = self.inherit_array_if_none(array)
        my_array = []
        for i in array:
            if i[element] == equal_to:
                my_array.append([True])
            else:
                my_array.append([False])
        return my_array  # Return array bool values in array

    def bigger_than(self, element: int, bigger_than: int, array: list = None) -> list:
        array = self.inherit_array_if_none(array)
        my_array = []
        for i in array:
            if i[element] > bigger_than:
                my_array.append([True])
            else:
                my_array.append([False])
        return my_array  # Return array bool values in array

    def smaller_than(self, element: int, smaller_than: int, array: list = None) -> list:
        array = self.inherit_array_if_none(array)
        my_array = []
        for i in array:
            if i[element] < smaller_than:
                my_array.append([True])
            else:
                my_array.append([False])
        return my_array  # Return array bool values in array

    def array_sum_values(self, array: list = None) -> list:
        array = self.inherit_array_if_none(array)
        my_array = []
        for i in array:
            amount = [0]
            for o in i:
                amount[0] += o
            my_array.append(amount.copy())
        return my_array  # Return array values in array [[3], [5]]

    def different_values(self, array: list = None) -> list:
        array = self.inherit_array_if_none(array)
        my_array = []
        for i in array:
            if i[0] != i[1]:
                my_array.append(i.copy())
        return my_array

    def any_is(self, array: list = None, value: int = None) -> list:
        array = self.inherit_array_if_none(array)
        i = 0
        my_array = []
        while i < len(array):
            my_array.append([False])
            i += 1
        i = 0
        while i < len(array[0]):
            my_array = self.array_or(my_array, self.equal_to(i, value, array))
            i += 1

        return my_array  # Return array bool values in array

    # Logic on arrays

    @staticmethod
    def array_or(array_bool1: list, array_bool2: list) -> list:
        my_array = []
        i = 0
        while i < len(array_bool1):
            if array_bool1[i][0] or array_bool2[i][0]:
                my_array.append([True])
            else:
                my_array.append([False])
            i += 1
        return my_array

    @staticmethod
    def array_and(array_bool1: list, array_bool2: list) -> list:
        my_array = []
        i = 0
        while i < len(array_bool1):
            if array_bool1[i][0] and array_bool2[i][0]:
                my_array.append([True])
            else:
                my_array.append([False])
            i += 1
        return my_array

    # For less redundancy

    def inherit_array_if_none(self, array):
        if array is None:
            array = self.array
        return array
