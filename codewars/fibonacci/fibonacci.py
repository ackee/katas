def fibonacci(n):
    return go(n, 0, 1)

def go(n, a, b):
    if n == 0:
        return a
    if n == 1:
        return b
    return go(n-1, b, a+b)
    
