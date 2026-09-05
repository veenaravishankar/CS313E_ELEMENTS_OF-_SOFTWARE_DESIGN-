"""
File: 2d_list.py
Course: C S 313E
Description: Solution for Week 2 Lecture 2 Activity - 2D List
"""

# Instructions: Write a Python program that processes a 3×3 matrix.

# Examine each element at position (i, j) and apply the following rules:
# 1. If (i + j) is even, double the element.
# 2. If i > j, add 3 to the element.
# 3. If the element is on the anti-diagonal, subtract 1 from it.
#   (Anti-diagonal: where column index is j == n - 1 - i),
#   meaning i + j == n - 1)

# Perform three additional custom updates to specific matrix elements.

def process_matrix(in_mat: list) -> list:
    """
    Takes input matrix and returns processed matrix.

    Parameters
    ----------
    in_mat: lst
        Matrix to be processed.

    Returns
    ----------
    out_mat: lst
        Processed matrix.
    """
    n = len(in_mat)    # for an n×n matrix
    out_mat = in_mat.copy()

    # passes have been consolidated into one nested for loop
    for i, _ in enumerate(in_mat):
        for j, _ in enumerate(in_mat[i]):
            # rule 1
            if (i + j) % 2 == 0:
                out_mat[i][j] *= 2
            # rule 2
            if i > j:
                out_mat[i][j] += 3
            # rule 3
            if (i + j) == (n - 1):
                out_mat[i][j] -= 1

    # three freestyle changes!
    out_mat[1][2] = int(input("Enter any whole number: "))
    out_mat[2][0] *= out_mat[2][2]
    out_mat[0][1] //= 3

    return out_mat


def main():
    """
    Main function runs process_matrix() and prints its result.
    """
    mat = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

    new_mat = process_matrix(mat)

    for row in new_mat:
        print(row)


if __name__ == '__main__':
    main()
