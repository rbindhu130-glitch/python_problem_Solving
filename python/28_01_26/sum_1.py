# n = 5

# for i in range(n):
#     for ch in range(i):
#         print(" ", end="")
#     print(n - i)



# n = 3

# # upper part
# for i in range(1, n + 1):
#     print(" " * (n - i), end="")
#     print("*", end="")
#     if i > 1:
#         print(" " * (2*i - 3) + "*")
#     else:
#         print()

# # lower part
# for i in range(n - 1, 0, -1):
#     print(" " * (n - i), end="")
#     print("*", end="")
#     if i > 1:
#         print(" " * (2*i - 3) + "*")
#     else:
#         print()





def zero(matrix):
    if len(matrix) == 0:
        return "Invalid Input"

    zero_count = 0

    # count how many zeros
    for i in range(0, len(matrix), +1):
        for j in range(0, len(matrix[0]), +1):
            zero_count = zero_count + (matrix[i][j] == 0)

    # zero_count > 0 → make everything 0
    keep = zero_count == 0   # True = 1, False = 0

    for i in range(0, len(matrix), +1):
        for j in range(0, len(matrix[0]), +1):
            matrix[i][j] = matrix[i][j] * keep

    return matrix


print(zero([[1,2,3],[4,0,6],[7,8,9]]))
print(zero([[1,2,3],[4,9,6],[7,8,9]]))

