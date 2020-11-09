a = [1, 3, 5, 7, 9, 11, 14, 16]
def bound(v, a):
    if v < a[0] or v > a[-1]:
        return False
    return True

def chop(v, arr):
    if not bound(v, arr):
        return -1
    i = int(round(len(arr)/2))
    if v == arr[i]:
        return i
    if v < arr[i]:
        return chop(v, arr[:i])
    if v > arr[i]:
        return chop(v, arr[i:]) + i #+i gör att returvärdet -1 vid error förstörs.
    return -1

