def convert(a, b):
    a = abs(int(a))
    b = abs(int(b))
    if a > b:
        a, b = b, a
    return a, b

def func1(a, b):
    lst = list(range(a, b+1))
    return sum(lst)

# MAIN FUNCTION
a = 1
b = 5
a, b = convert(a, b)
print(func1(a, b))
