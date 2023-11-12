def isPalindrome(s, m=0, n=None):
    if n is None:
        n = len(s) - 1

    if m < n:
        if s[m] == s[n]:
            return isPalindrome(s, m + 1, n - 1)
        else:
            return False
    else:
        return True

user_input = input("Enter your string: ")

if isPalindrome(user_input):
    print("Given string is a palindrome")
else:
    print("Given string is not a palindrome")
