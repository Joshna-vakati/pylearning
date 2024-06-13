#4. Fibonaci series
# 0,0+1, 0+1+1,
# n = 7
# 0, 1 , 1, 2, 3,5,8,13,21

n = int(input("Enter the number"))
a = 0
b = 1
for i in range(n+1):
    if i == 0:
        print(a, end =' ')
    elif i ==1:
        print(b, end =' ')
    else:
        fib = a+b       #1
        print(fib, end =' ')
        a, b  = b, fib


