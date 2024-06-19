def my_func(*args):
    print(args)
    for i in range(len(args)):
        print(args[i])

my_func(1,2,3,4,5)

# *args ->
# Non keyword arguments
# recives arguments as tuple
#captures arguments as positional arguments

# **kwargs ->
# keyword arguments
# recieves arguments as dictionary
# captures arguments as keyword arguments


def func(*argv,**kwarg):
    print(argv)
    print(kwarg)

func(1,2,3,4,5, name ='Joshna', age ='4')
