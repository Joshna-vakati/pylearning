# finally keyword
#  which is always executed after the try and except blocks.
#  #The final block always executes after the normal termination of the try block or
#  after the try block terminates due to some exception.

try:
    a = 10 / 0
except Exception as e:
    print(e)
else:
    print("else block")
finally:
    print("finally block")