#A zero-indexed array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.
#
#Your goal is to find that missing element.
#
#Write a function:
#
#    int solution(int A[], int N);
#    that, given a zero-indexed array A, returns the value of the missing element.
#
#    For example, given array A such that:
#
#          A[0] = 2
#            A[1] = 3
#              A[2] = 1
#                A[3] = 5
#                the function should return 4, as it is the missing element.
#
#                Assume that:
#
#                    N is an integer within the range [0..100,000];
#                    the elements of A are all distinct;
#                    each element of array A is an integer within the range [1..(N + 1)].
#                    Complexity:
#
#                        expected worst-case time complexity is O(N);
#                        expected worst-case space complexity is O(1), beyond input storage (not counting the storage required for input arguments).


def solution(A):
    # write your code in Python 3.6
    N = len(A)
    if N == 0:
        return 1
    for i in range(N):
        if abs(A[i]) > N:
            pass
        else:
            A[abs(A[i])-1] = -A[abs(A[i])-1]
    for i in range(N):
        if A[i] > 0:
            return i+1
    
    return N+1

print(solution([2, 3, 1, 5]))
print(solution([]))
print(solution([3,5,4,1,2]))

