def solution(A, B, K):
    # write your code in Python 3.6
    ans = ((B // K) - (A // K))
    return ans + 1 if A % 2 == 0 else ans 