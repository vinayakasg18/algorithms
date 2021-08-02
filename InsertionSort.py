"""Class to sort the list using insertion sort"""
# import logging as log


class InsertionSort:
    """ Function to sort the input array using Insertion Algorithm """
    def insertionsort(self, a):

        assert (isinstance(a, list)), "Make sure the input is a type of list"

        if not a:
            # log.info("Returning a empty list")
            return []

        if '' in a:
            # log.error("List must contain the integer values")
            raise ValueError

        # Sorting by comparing the values left to the key value

        # assert self.sorted(0, a[0])

        for index in range(1, len(a)):
            # assert sorted(a, 0, index - 1)
            key = a[index]
            while index > 0 and a[index - 1] > key:
                a[index] = a[index - 1]
                index = index - 1
            a[index] = key
            # assert sorted(a[0], a[index])
        return a


if __name__ == "__main__":
    array = [5, 2, 4, 1, 1]
    print(InsertionSort().insertionsort(array))
