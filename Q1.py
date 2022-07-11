def get_pairs_with_total(num_pairs, total):
    """returns a list of tuples whereby num1 + num2 is equals to the total"""
    final_list = []
    for each_tuple in num_pairs:
        num1 = each_tuple[0]
        num2 = each_tuple[1]
        if num1 + num2 == total:
            final_list.append(each_tuple)
    return final_list

print(get_pairs_with_total([(3,4), (5,4), (3,3), (2,0), (5,2), (1,6)], 7))
print(get_pairs_with_total([(1,4), (5,4), (3,3), (2,0), (5,-9)], 7))
