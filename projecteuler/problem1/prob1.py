def multiple(num):
    if num % 3 == 0 or num % 5 == 0:
        return True
    return False

sum = 0
for i in range(1000):
    if multiple(i):
        sum += i

print(sum)
