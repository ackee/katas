def narcissistic(value):
    digits = numtodigitslist(value)
    if cubedsum(digits) == value:
        return True
    return False

def numtodigitslist(num):
    return [int(d) for d in str(num)]

def cubedsum(dlist):
    return sum(list(map(lambda x: x**len(dlist), dlist)))
