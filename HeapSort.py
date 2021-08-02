""" HeapSort Class """
class HeapSort:

    def heapify(self, A, n, i):
        """ Function to sort using HeapSort """

        largest_value = i
        
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        if left_child < n and A[i] < A[left_child]:
            largest_value = left_child

        if right_child < n and A[largest_value] < A[right_child]:
            largest_value = right_child

        if largest_value != i:
            A[i],A[largest_value] = A[largest_value],A[i]
            self.heapify(A, n, largest_value)


    def heapSort(self, A):

        n = len(A)

        # max-heap
        for i in range(n, -1, -1):
            self.heapify(A, n, i)

        # Remove the largest elements in the process.
        for i in range(n - 1, 0, -1):
            A[i], A[0] = A[0], A[i]
            self.heapify(A, i, 0)

# A = [10, 6, 7, 5, 15, 17, 12]
# print(HeapSort().heapSort(A))
