# NOTES:
#   Insertion sort is a simple but inefficient algorithm. It should only be used when the input size is small
#   and the algorithm is not used often.
#
# INPUT: an array of numbers, A[0..n]
# OUTPUT: an ordered array of numbers, A[0..n]
#
# PSEUDOCODE:
#  insertion_sort(A):
#    for i := 1 to length of A         //We start as A[1] so we can compare it to the previous element A[0]
#        key := A[i]                   //Our loop allows us to check every element in the array
#        j := i - 1
#        while j >= 0 and A[j] > key   //This is our comparison. If all previous elements to the current
#          A[j+1] := A[j]              //If one is greater than the current we swap them.
#          j--
#        A[j+1] := key                  //We are finished with the current key. Increment to the next one.
#     return A
#
# ANALYSIS:
#   Best T(n) (Big-Omega):  O(n)
#   Worst T(n) (Big-O):     O(n^2)
#   Average T(n):           O(n^2)


def insertion_sort(A):
    for i in range(1, len(A)):  # Python syntax needs 'range' to get the index and 'len' to get the # of elements in A
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
    return A


if __name__ == "__main__":
    A = [10, 12, 99, 1, 0, 1, -5, 79]
    print("Sorting {0}".format(A))
    print(insertion_sort(A))


