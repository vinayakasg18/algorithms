""" Class to count the inversion count using merge sort"""


class InversionCount:
    def count(self, A: [int]) -> [int]:
        """ Count and return the array containing the count of each element """

        index_array = []
        rc_arr = []
        for ind in range(0, len(A)):
            index_array.append(ind)
            rc_arr.append(0)
        self.sort(A, index_array, 0, len(index_array) - 1, rc_arr)
        return rc_arr

    def merge(self, A, ind, p, q, r, rc_array):
        """ This method does the same work as mergeSort but we will be checking for the inversion and increase the
        count """

        left = ind[p:q + 1]
        right = ind[q + 1:r + 1]

        i = 0
        j = 0
        ic = 0
        k = p

        while i < len(left) and j < len(right):
            if A[left[i]] > A[right[j]]:
                ind[k] = right[j]
                ic += 1
                k += 1
                j += 1
            else:
                rc_array[left[i]] = rc_array[left[i]] + ic
                ind[k] = left[i]
                i += 1
                k += 1

        while i < len(left):
            rc_array[left[i]] = rc_array[left[i]] + ic
            ind[k] = left[i]
            k += 1
            i += 1
        while j < len(right):
            ind[k] = right[j]
            k += 1
            j += 1

    def sort(self, A, index, p, r, rc_arr):
        """Function to Divide the input Array into equal sub-arrays"""

        if p < r:
            q = (p + r) // 2

            self.sort(A, index, p, q, rc_arr)
            self.sort(A, index, q + 1, r, rc_arr)
            self.merge(A, index, p, q, r, rc_arr)


if __name__ == "__main__":
    A = [5, 10, 4, 7, 9, 2, 1, 0]
    print(InversionCount().count(A))
