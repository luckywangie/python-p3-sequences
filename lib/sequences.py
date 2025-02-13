def print_fibonacci(length):
    fib_sequence = []
    a, b = 0, 1
    while len(fib_sequence) < length:
        fib_sequence.append(a)
        a, b = b, a + b
    print(fib_sequence)



# function test
print_fibonacci(9)
