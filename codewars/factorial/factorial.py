def factorial(n):
    return go(n-1,n)

def go(n, acc):
    if n <= 1:
        return acc
    return go(n-1,n*acc)
