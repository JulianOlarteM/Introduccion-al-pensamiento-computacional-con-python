def factorial(n):
    """Calcula el factorial de n.
    n int > 0
    return n!
    """
    print(n)
    if n==1:
        return 1 # porque facotrial de 1 es igual a 1
    return n * factorial(n-1)

n = int (input('Escribe un entero: '))
print(factorial(n))

