def encode(message, num_rows):
    # STEP 1: Remove all non-alphanumeric chars
    new_string = ""
    chars_in_message = list(message)
    for each_char in chars_in_message:
        if each_char.isalnum():        # if True
            new_string += each_char
    # STEP 2: Capitalize all letters
    new_string = new_string.upper()
    # STEP 3: Arrange the str on the 7x7 (7 is num_rows) grid (rotate pic in qn 90 degree clockwise)
    # --> Column 1 will now be Row 1, Col 2 -> Row 2 etc
    # Letters are now arranged starting from row0, col0 to col6,
    # then from row1, col6 to col0, then from row2, col0 to col6 etc
    # empty spot will be filled with '#' until num_rows x num_rows is filled fully
    # Probably use an array where each list represents each row
    array_eg = []
    for each_list in range(num_rows):      # number of each_list = num_rows
        array_eg.append([])                # create no. of [] = num_rows
    # In array_eg, first list represents first row, number of letters/elements in
    # each row is equal to number of columns(same as num_rows)
    for each_list in array_eg:

    print(array_eg)
    return new_string
print(encode("The stars must be jealous. You shine way better than they do!", 7))

# LEFTOVER ISSUE: Need to find a wa to maybe put on a matrix first.
# Then, if digits not in final_str yet, append letter to final_str
# in a clockwise direc from outer to inner