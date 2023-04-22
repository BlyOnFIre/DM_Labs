import itertools
import numpy as np


def init_data():
    # Read the matrices from files
    matrixA = read_int_matrix("l5_a.txt")
    matrixB = read_int_matrix("l5_b.txt")

    # Get the size of the matrices
    matrixSize = len(matrixA)

    # Create a list of indices for permutations
    permutations = list(range(matrixSize))

    return matrixA, matrixB, matrixSize, permutations


def match(matrixA, matrixB, matrixSize, permutations):
    # Compare the elements in A and B according to the current permutation
    for i in range(matrixSize):
        for j in range(matrixSize):
            if matrixA[i][j] != matrixB[permutations[i]][permutations[j]]:
                return False
    return True


def solve(matrixA, matrixB, matrixSize, permutations):
    # Iterate through all possible permutations of the indices
    for perm in itertools.permutations(permutations):
        permutations = list(perm)

        # Check if the current permutation leads to a match
        if match(matrixA, matrixB, matrixSize, permutations):
            # Print the matching permutation
            for i in range(matrixSize):
                print(f"{{{i + 1}: {permutations[i] + 1}}}; ", end="")
            break


def read_int_matrix(path):
    # Read the file and split the lines
    with open(path, "r") as f:
        lines = f.readlines()

        # Get the size of the matrix from the first line
        n = int(lines[0].strip())

        # Initialize the matrix with zeros
        matrix = np.zeros((n, n), dtype=int)

        # Fill the matrix with values from the file
        for i, line in enumerate(lines[1:]):
            matrix[i] = list(map(int, line.strip().split(" ")))
    return matrix


if __name__ == "__main__":
    # Initialize the data
    matrixA, matrixB, matrixSize, permutations = init_data()

    # Find a matching permutation and print the result
    solve(matrixA, matrixB, matrixSize, permutations)
