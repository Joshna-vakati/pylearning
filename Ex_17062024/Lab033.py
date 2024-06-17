def f1(a, b, c):
    print(a, b, c)
    return a + b + c


print("End")

# result = f1(3, 4, 5)
# result = f1(a=4, b=6, c=9)
# result = f1(b=6, a=4, c=9)
result = f1(1,2,3)
print(result)





# *args - any number of arguments
# print("Pramod", "Amit", "SB")


def sum_three(a=1, b=1, c=1):
    return a + b + c


# result = sum_three()
result1 = sum_three()
result2 = sum_three(1,2)
result3 = sum_three(1,2,3)
result4 = sum_three(a=10,b=67,c=45)
result5 = sum_three(b=67,a=10,c=45)
print(result1,result2,result3,result4,result5)
