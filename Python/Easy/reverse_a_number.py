def reverse_number(num):
    back = str(num)
    if back.find('-') != -1:
        wards = back.replace('-', '')[::-1]
        if back.find('.') != -1:
            return float('-' + wards)
        elif back.find('.') == -1:
            return int('-' + wards) if num != 0 else int
    else:
        if back.find('.') != -1:
            return float(back.replace('0', '')[::-1])
        else:
            return int(back.replace('0', '')[::-1]) if num != 0 else int()