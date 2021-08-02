"""Class to sort the Array using merge sort algorithm(Divide and conquer)"""


class MergeSort:
    def merge(self, A, p, q, r):
        """Function to Merge and sort the sub arrays"""

        left = A[p:q + 1]
        right = A[q + 1:r + 1]

        i = 0
        j = 0
        k = p

        assert sorted(left)
        assert sorted(right)

        while i < len(left) and j < len(right):
            # assert sorted(left[i:p]) and sorted(right[i:j])
            if left[i] < right[j]:
                A[k] = left[i]
                k += 1
                i += 1
            else:
                A[k] = right[j]
                j += 1
                k += 1

        while i < len(left):
            A[k] = left[i]
            k += 1
            i += 1
        while j < len(right):
            A[k] = right[j]
            k += 1
            j += 1

        # assert sorted(A) == A[p:r+1]

    def sort(self, A, p, r):
        """Function to Divide the input Array into equal sub-arrays"""

        if p < r:
            q = p + (r - p) // 2

            self.sort(A, p, q)
            self.sort(A, q + 1, r)
            self.merge(A, p, q, r)

    # def is_sorted(self, A):
    #     for i in range(0, len(A)):
    #         assert A[i] <= A[i - 1]


if __name__ == "__main__":
    A = [8, 4, 1, 2, 9, 0]
    MergeSort().sort(A, 0, len(A) - 1)
    print(A)
