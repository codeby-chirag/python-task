class Matrix:
    def add_matrix(m1, m2):
        addition = []

        for i in range(3):
            row = []
            for j in range(3):
                row.append(m1[i][j] + m2[i][j])
            addition.append(row)

        print(addition)
        

limit = 3

print("Enter each row with", limit, "values separated by spaces:")
mat1 = [list(map(int, input().split())) for _ in range(limit)]
print(mat1)

print("Enter each row with", limit, "values separated by spaces:")
mat2 = [list(map(int, input().split())) for _ in range(limit)]
print(mat2)

x = Matrix().add_matrix(mat1, mat2)
# x.add_matrix()

# mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# mat2 = [[8, 5, 9], [7, 5, 3], [9, 5, 1]]

# addition = []

# for i in range(3):
#     row = []
#     for j in range(3):
#         row.append(mat1[i][j] + mat2[i][j])
#     addition.append(row)

# print(addition)


# for i in range(3):
#     print("row:",i)
    
# for j in range(4):
#     # print(mat[i][j])
#     print("\nmat=",mat1)# total list
#     print("\nmat[0]=",mat1[0])#first row
#     print("\nmat[0][2]=",mat1[0][2])# getting specific element
#     print("\nmat[1][-1]=",mat1[1][-1]) # last element in second row