def rotate(mat):
    # create a deepcopy of matrix 
    copy = [row[:] for row in mat]
    
    # modifying original matrix
    for row in range(len(mat)):
        for column in range(len(mat[0])):
            mat[row][column] = copy[len(mat) - 1 - column][row]
    
    return mat

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Looks like
# 1 2 3
# 4 5 6
# 7 8 9

# Rotated looks like
# 7 4 1
# 8 5 2
# 9 6 3
# new row0 = elements from old col0 inversed
# new row1 = elements from old col1 inversed
# new row2 = elements from old col2 inversed
# --> new row = old col inversed
print(rotate(mat))
# [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
