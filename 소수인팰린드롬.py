def isPalindrome(s):
    left = 0
    right = len(s)-1
    while left <= right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


a,b = map(int, input().split())
if b > 9989899:
    b = 9989899
arr = [False, False] + [True] * (b + 1)

for i in range(2, b+1):
    if arr[i]:
        for j in range(i+i, b+1, i):
            arr[j] = False


for i in range(a, b+1):
    if arr[i] and isPalindrome(str(i)):
        print(i)
print(-1)

