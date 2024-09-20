def pertence_fibonacci(numero):
    if numero < 0:
        return False
    fib1, fib2 = 0, 1
    while fib2 < numero:
        fib1, fib2 = fib2, fib1 + fib2
    return fib2 == numero

numero = 21

if pertence_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")
