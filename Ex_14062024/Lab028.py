# break statement

# used to terminate the loop or statement in which it is present.
# control will pass to the statements that are present after the break statement, if available

# syntax :
#
# for loop:
#     if condition:
#         break
#     statement
# loop end


# for example,

for i in range(10):
    print(i)
    if i==6:
        break

print('a'*50)

for i in range(10):
    if i==6:
        break
    print(i)

