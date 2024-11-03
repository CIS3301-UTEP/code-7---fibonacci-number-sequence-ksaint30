def fibo_numb_wit_recursion(number):
    if number == 0:
        return 0
    if number == 1:
        return 1
    
    return fibo_numb_wit_recursion(number-1)\
            +fibo_numb_wit_recursion(number-2)

print(fibo_numb_wit_recursion(6))