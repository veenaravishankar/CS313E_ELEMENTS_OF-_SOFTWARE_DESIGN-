"""
File: ramp_input_loop.py
Course: C S 313E
Description: Solution for Week 1 Lecture 2 Activity - On-Ramp
"""

# Instructions: Validate input using a loop.
# Keep asking until the user gives a whole number between 1 and 100
# (assume inclusive), then return it.
# No exceptions yet - use only what we covered today.

# What should the loop condition should be? Do we even need one at all?

# Since there is more than one condition we need to check for,
# we can use branching within the loop instead.

def get_valid_number():
    """
    Receive a whole number between 1 and 100 and return the valid input.

    Returns
    -------
    num: str
        User input.
    """
    # setting the while condition to True makes the loop run indefinitely
    while True:
        num = input('Enter a whole number between 1 and 100: ')
        # checks that input is a number
        if not num.isdigit():
            continue
        # checks if number is within bounds
        if 1 <= int(num) <= 100:
            # only the return statement can end the indefinite loop
            return num

def main():
    """
    Main function that runs get_valid_number() and prints result.
    """
    valid_num = get_valid_number()
    print(f"{valid_num} is a valid number.")

if __name__ == '__main__':
    main()
