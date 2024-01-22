def isPalindrome(s):
    return s == s[::-1]


s = "malayalm"
ans = isPalindrome(s)

if ans:
    print("Yes")
else:
    print("No")
