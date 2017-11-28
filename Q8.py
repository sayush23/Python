def fib(num):
    list = []
    a = 1
    b = 1
    list.append(a)
    list.append(b)
    for i in range(0, (num-2)):
        s = b + a
        list.append(s)
        a = b
        b = s
    return list
num = int(input("Enter number of terms"))
print(fib(num))