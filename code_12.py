def get_fibonacci_number(position):
    if position == 0:
        return 0
    if position == 1:
        return 1
    
    return get_fibonacci_number(position-1)\
            +get_fibonacci_number(position-2)

def get_fibonacci_number_sequence(number):
    list = []
    for x in range(1,number+1):
        list.append(get_fibonacci_number(x))
    return list

if __name__ == "__main__":
    number = 7
    print(get_fibonacci_number(number))
    print(get_fibonacci_number_sequence(number))