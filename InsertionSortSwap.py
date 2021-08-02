class InsertionSort:
    """ Function to sort the input array using Insertion Algorithm """
    def insertionsort(self, a):

        if not a:
            return []
        #  0  1  2  3  4  5
        # [5, 2, 4, 1, 0, 2]
        # [2, 5, 4, 1, 0, 2]
        # [2, 4, 5, 1, 0, 2]

        for index in range(1, len(a)):
            # sorted(0, index - 1) -- works
            key = a[index]

            while index > 0 and key < a[index - 1]:
                a[index - 1], a[index] = a[index], a[index - 1]
                # sorted(index - 1, index) -- wrong
                index = index - 1
        return a


if __name__ == "__main__":
    array = [5, 2, 4, 1, 1, 9]
    print(InsertionSort().insertionsort(array))
