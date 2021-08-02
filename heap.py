def heapify(A, n, i):

    mid_value = n // 2

    left = 2 * i + 1
    right = 2 * i + 2
    parent = (mid_value - 1) // 2

    while A.index(A[mid_value]) < i:

        if A[parent] < A[mid_value]:
            A[mid_value], A[parent] = A[parent], A[mid_value]

        elif A[right] > A[mid_value]:
            A[right], A[mid_value] = A[mid_value], A[right]

        mid_value -= 1




def heapSort(A):

    n = len(A)
	
    # max-heap
    for i in range(len(A), -1, -1):
        heapify(A, n, i)

    for i in range(n - 1, 0, -1):
        A[i], A[0] = A[0], A[i]
        heapify(A, n, i)

A = [ 12, 11, 13, 5, 6, 7]
heapSort(A)
