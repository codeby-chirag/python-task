"""Perform operations like Addition & Multiplication on entered 3x3 Matrix."""


class Matrix:
    """Class which store the function of addition & multiplication."""
    
    def add_matrix(self, m1, m2):
        """Add the matrix."""
        addition = []

        for i in range(3):
            row = []
            for j in range(3):
                row.append(m1[i][j] + m2[i][j])
            addition.append(row)

        print(f"\nAddition of Matrix: {addition}")

    def mul_matrix(self, m1, m2):
        """Multiply the matrix."""
        multiply = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        for i in range(len(m1)):
            for j in range(len(m2[0])):
                for k in range(len(m2)):
                    multiply[i][j] += m1[i][k] * m2[k][j]

        print(f"\nMultiplication of Matrix: {multiply}")


def validate_matrix(matrix):
    """Validate input matrix."""
    new_matrix = []
    if len(matrix) != 3:
        print("Matrix must be 3x3")
        y = [list(input().split()) for x in range(limit)]
        return validate_matrix(y)

    for row in matrix:
        if len(row) != 3:
            print("Matrix must be 3x3")
            y = [list(input().split()) for x in range(limit)]
            return validate_matrix(y)

        new_row = []
        for item in row:
            try:
                new_row.append(float(item))
            except ValueError:
                print("Value must be intiger or float")
                y = [list(input().split()) for x in range(limit)]
                return validate_matrix(y)

        new_matrix.append(new_row)

    print(f"Matrix : {new_matrix}")
    return new_matrix


limit = 3

print("Enter each row with", limit, "values separated by spaces:")
mat1 = [list(input().split()) for x in range(limit)]
mat1 = validate_matrix(mat1)

print("\nEnter each row with", limit, "values separated by spaces:")
mat2 = [list(input().split()) for x in range(limit)]
mat2 = validate_matrix(mat2)

x = Matrix()
x.add_matrix(mat1, mat2)
x.mul_matrix(mat1, mat2)
