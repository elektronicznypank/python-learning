def format_number(num):
    num = str(num)
    rev_num = num[::-1]
    rev_formatted_num = ''
    for i in range(len(num)):
        print(i)
        if i % 3 == 0 and i != 0:
            rev_formatted_num += ','
        rev_formatted_num += rev_num[i]
    formatted_num = rev_formatted_num[::-1]
    return formatted_num
