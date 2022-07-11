def get_valid_ip_addresses(addr_list):
    final_list = []
    for each_ip in addr_list:
        each_ip_splitted = each_ip.split('.')    # split into a list separated by '.
        for each_number in each_ip_splitted:
            if each_number.isnumeric() == True:  # only if is a number, not alphabet etc
                if int(each_number) >= 0 and int(each_number) <= 255:  # if is a valid number
                    continue
                else:
                    break            # get out of current iteration once one number invalid
            else:
                break                # if each_number is not a number
        else:  # *** Using for else--> else only executed if break statement not encountered in 'for' loop
            final_list.append(each_ip)
    return final_list

print(get_valid_ip_addresses(['10.10.10.10', '0.0.0.0', '99.7.7.299']))
print(get_valid_ip_addresses(['999.10.10.10', '-1.0.0.0', 'a.10.a.a']))