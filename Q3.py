def rotate(matrix):
    """function will rotate a matrix by 90 degrees in anti-clockwise direction"""
    final_matrix = []
    # STEP 1: # iterate from len of first list in matrix to 0, step of -1
    for i in range(len(matrix[0]), 0, -1):     # e.g: range(3,0,-1)---> i=3,2,1,0
        # STEP 2: Create lambda function--> that minus 1 off value of i, x will be each list in matrix
        lambda_function = lambda x : x[i - 1]
        # STEP 3: use map() to apply lambda_function to each item (x) of the iterable (matrix)
        new_rotated_as_object = map(lambda_function, matrix)  # return is a map object
        # STEP 4: Converting to list
        new_rotated_list = list(new_rotated_as_object)
        final_matrix.append(new_rotated_list)
    return final_matrix
 j
print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(rotate([[1, 2], [4, 5], [7, 8]]))
# LEFTOVER ISSUE: Got answer from stackover, need explanation