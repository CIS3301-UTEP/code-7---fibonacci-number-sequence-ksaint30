def get_fibonacci_number(position):
    if position == 0:
        return 0
    if position == 1:
        return 1
    
    return get_fibonacci_number(position-1)\
            +get_fibonacci_number(position-2)

def get_fibonacci_number_sequence(number):
    if number == 0:
        return [1]
    if number == 1:
        return [1,1]
    list = get_fibonacci_number_sequence(number-1)
    if len(list) < number:
        return list
    list.append(list[-1] + list[-2])
    return list

if __name__ == "__main__":
    print(get_fibonacci_number(4))
    print(get_fibonacci_number_sequence(4))