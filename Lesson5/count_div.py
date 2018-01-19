#Write a function:

#int solution(int A, int B, int K);
#that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:
#
#    { i : A ≤ i ≤ B, i mod K = 0 }
#    For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.
#
#    Assume that:
#
#        A and B are integers within the range [0..2,000,000,000];
#        K is an integer within the range [1..2,000,000,000];
#        A ≤ B.
#        Complexity:
#
#            expected worst-case time complexity is O(1);
#            expected worst-case space complexity is O(1).


from math import floor

def solution(A, B, K):
    # write your code in Python 3.6
    if B == 0:
        return 1
    elif K > B:
        return 0
    elif K > A:
        ans = floor(B/K)
    elif A > 0:
        ans = floor(B/K) - floor((A-1)/K)
    else:
        ans = floor(B/K)

    if A == 0:
        ans +=1

    return ans



