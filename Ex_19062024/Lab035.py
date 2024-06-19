
numbers =[1,2,3,4]            #1

def add_list(lst):          #4
    lst.append(4)           #5
    return lst              #6

numbers.append(6)           #2
l = add_list(numbers)       #3
print(l)                    #7