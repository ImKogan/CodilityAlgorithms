#This is a demo task.
#
#Write a function:
#
#    int solution(int A[], int N);
#    that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
#
#    For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
#
#    Given A = [1, 2, 3], the function should return 4.
#
#    Given A = [−1, −3], the function should return 1.
#
#    Assume that:
#
#        N is an integer within the range [1..100,000];
#        each element of array A is an integer within the range [−1,000,000..1,000,000].
#        Complexity:
#
#            expected worst-case time complexity is O(N);
#            expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).


def solution(A):
    # write your code in Python 3.6
    N = len(A)
    d = {}
    for i in range(N):
        if A[i] > 0:
            if d.get(A[i]) == None:
                d[A[i]] = 1

    for i in range(1,len(d)+1):
        if d.get(i) == None:
            return i

    return len(d) + 1
