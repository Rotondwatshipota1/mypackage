def sum_array(array):
    '''''
    this funtion ruturns  the sum of the elments in an sum_array

    args : array it accepts an array as an argument
    returns : n the sum of elements in an sum_array
    ''''
    for i in array:
        return sum_array(array)

def fibonacci(n):
    ''''
    this funtion returns the nth fibonacci number
    Args: int n the nth position of the sequence
    returns the number in the nth index of the fibonacci sequence
    ''''
    if n <= 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def factorial(n):
    '''' this funtion returns the factorial of a give n intheger
    args: n it accepts an intger n as its argument
    returns : the number or the factorial of the given number
    ''''
    if n < 1:
        return 1
    else:
        return n * factorial(n-1)

def reverse(word):
    ''''
    this funtion returns a word in a reverse order
    args : word it accepts a word as its argument
    return: it returns a given word in a reverse order
    ''''
    if word == "":
        return word
    else:
        return reverse(word[1:]) + word[0]
