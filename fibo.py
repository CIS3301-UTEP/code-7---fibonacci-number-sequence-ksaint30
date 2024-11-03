# def get_fibonacci_number(number):
#     if number == 0:
#         return 0
#     if number == 1:
#         return 1
    
#     prev_a = 0
#     prev_b = 1

#     for x in range(2,number+1):
#         current_fibo_number = prev_a + prev_b
#         prev_a = prev_b
#         prev_b = current_fibo_number
    
#     return prev_b

def get_fibonacci_sequence(n):
    if n == 0:
        return [0]
    if n == 1:
        return [0,1]
    
    prev_x = 0
    prev_y = 1

    number_sequence = [0,1]
    
    for i in range(2, n+1):
        current = prev_x + prev_y
        prev_x = prev_y
        prev_y = current  

        number_sequence.append(current)
    return number_sequence    
# print(get_fibonacci_number(4))
print(get_fibonacci_sequence(5))