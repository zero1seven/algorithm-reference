# NOTES:
#    It's easier to visualize a heapsort in terms of a binary tree. However there are benefits to using an array
#    to represent the binary tree. The most obvious is that you may not receive a tree for input.
#    But another reason is that in order to find an element in the middle of a tree I can do a simple
#    calculation rather than walk the path of the tree. We will be using and array to represent the binary tree
#    and the heapsort algorithm. Please look up resources to visualize the procedure in terms of a binary tree.
#
#    In order to achieve the sort we need to define the heap_sort, build_heap (max), and heapify functions. Heapify
#    allows us to maintain the properties of a max-heap.
#
#    Also note, the pseudocode is written A[1..n]. This is the format I normally see pseudocode written in
#    even though index 0 is in a typical implementation. For now, I'll translate this in the code. I may normalize
#    my pseudocode at a later time to avoid confusion.
#
#
# INPUT: an array of numbers, A[0..n]
# OUTPUT: an array of numbers representing a max heap, A[0..n]
#
# PSEUDOCODE:
#  heap_sort(A):
#    build_heap(A)                  //MAX heap. A min heap could also be used with other code modifications.
#    for i := length of A to 1
#      swap A[1] and A[i]           //The root is the biggest. so put it at the end of our sorted list
#      reduce length of A by 1      //ignore the end because it's that part is already sorted.
#      heapify(A,1)                 //The remaining tree may not be a max heap. heapify restores
#                                   //The heap property
#    return A
#
#  build_heap(A):
#    for i := length of A to 1      //go through the array and ensure each element matches the max heap properties
#       heapify(A)
#
#  heapify(A, i):                                  //i is the root.
#    left := i + 1                                 //left child
#    right := i + 2                                //right child
#    if A[left] exists and A[left] > A[i]          //find the largest of left, right, and parent
#      largest = left
#    else largest = right
#    if A[right] exists and A[right] > A[largest]
#      largest = right
#    if largest != i                               //If a child is bigger swap it and repeat
#       swap A[largest] and A[i]
#       heapify(A,largest)
#
#
# ANALYSIS:
#   Best T(n) (Big-Omega):  O(nLog(n))
#   Worst T(n) (Big-O):     O(nLog(n))
#   Average T(n):           O(nLog(n))

import math # Used for floor function


def heap_sort(A):
    A = build_heap(A)
    heap_size = len(A)                   # Implimentation specific. Allows me to track the size of my array without creating a new one
    for i in range(heap_size-1, 0, -1):  # loop from the largest index down to and including index 1.
        temp = A[i]                      # Swap A[i] and A[0]
        A[i] = A[0]
        A[0] = temp
        heap_size -= 1
        A = heapify(A, 0, heap_size)  # Again, I'd rather perform the sort in place so I added an extra parameter to track the heap size
    return A


def build_heap(A):                                               # Building a max heap.
    heap_size = len(A)
    for i in range(int(math.floor((heap_size - 1)/2)), -1, -1):  # Divide the array by 2. If it's odd, take the lower element. Also, I use the first '-1' so that the loop includes index 0
        A = heapify(A, i, len(A))                                # len(A) is only used because I needed to track the heap size in heap_sort
    return A


def heapify(A, i, heap_size):
    left_child = i + 1                                         # The left child is always the next index followed by the right child.
    right_child = i + 2
    if left_child < heap_size and A[left_child] > A[i]:        # If left child exists check if it's larger than the parent.
        largest = left_child
    else:
        largest = i
    if right_child < heap_size and A[right_child] > A[largest]:
        largest = right_child
    if largest != i:                                            # If there was a larger found, swap it in.
        temp = A[i]
        A[i] = A[largest]
        A[largest] = temp
        A = heapify(A, largest, heap_size)                      # ensure max heap property on new tree
    return A


if __name__ == "__main__":
    A = [10, 12, 99, 1, 0, 1, -5, 79, 100, 5, 1, 12, 42]
    print("Sorting {0}".format(A))
    print(heap_sort(A))