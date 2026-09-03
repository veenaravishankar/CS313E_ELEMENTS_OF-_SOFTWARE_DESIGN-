"""
File: four_slices.py
Course: C S 313E
Description: Solution for Week 2 Lecture 1 Activity - Four Slices
"""

# Instructions: t is a valid encoding of s if t can be formed from s by
# inserting extra characters anywhere in s while keeping the original characters
# of s in the same relative order.

# Examples:
# "abcde" is a valid encoding of "ace" (insert b and d).
# "abcde" is not a valid encoding of "aec" (order of characters is different).

# Input: s = "abc", t = "ahbgdc"
# Output: true

# Input: s = "axc", t = "ahbgdc"
# Output: false

def is_valid_encoding(s: str, t: str) -> bool:
    """
    Outputs true if t is a valid encoding of s and false otherwise.

    Parameters
    ----------
    s: str
        String to be compared against.
    t: str
        String to be validated as encoding of s.

    Returns
    ----------
    bool
    """
    # initialize pointers for each string
    i = 0
    j = 0

    # ensure pointers can't go out of bounds
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1    # increment i everytime there is a match
        j += 1    # increment j every iteration
    return i == len(s)


def main():
    """
    Main function that runs is_valid_encoding() and prints result.
    """
    s = input('Enter a string: ')
    t = input('Enter another string: ')

    if is_valid_encoding(s, t):
        print('t is a valid encoding of s')
    else:
        print('t is an invalid encoding of s')

if __name__ == '__main__':
    main()
