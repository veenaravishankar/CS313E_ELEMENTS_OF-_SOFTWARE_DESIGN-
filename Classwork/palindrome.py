# Return True if s is a palindrome.
# Case-insensitive. Letters only,
# no spaces or punctuation.

#   "abcbba"  -> False
#   "Racecar"  -> True

def isPalindrome(s: str) -> bool:
    l, r = 0, len(s)
    while l <= r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True
