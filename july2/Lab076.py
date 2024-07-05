# try and except statements
# try - statement can raise exception are kept inside the try clause
# except - catches the exception raised inside the try clause
a = 10
b = 0
try:
    c = a / b
    print(c)
except:
    print("Cannot divide with zero")
