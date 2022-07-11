def get_free_timings(file_name, target_building, target_facility, target_date):
    """returns a list of tuple of available timings for booking"""
    data = open(file_name)
    for each_line in data:
        each_line = each_line.rstrip('\n')         # to remove empty alternate line

        # Since each column separated by 1 or more whitespaces/tabs. Split by 1 whitespace first.
        # Afterwards, if char in each_line_splitted is ' ', remove that char in the list
        each_line_splitted = each_line.split(' ')  # get a list separated by ' '
        for each_char in each_line_splitted:
            if each_char == ' ':                   # remove char if char is whitespace
                each_line_splitted.remove(each_char)
        print(each_line_splitted)
 h
print(get_free_timings('bookings.txt', 'SIS', 'SR2.2', '12/12/2019'))
# LEFTOVER ISSUE: Need to find a way to identify n remove whitespace and '\t' from file