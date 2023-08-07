# try:
#     num = int(input("Enter a number to divide"))
#     num2 = int(input("Enter a number to divide"))
#     result = num/num2

#     print(result)

# except:
#     print("Cannot divide by zero")


try:
    even_number = [2,4,6,8,] # list of even numbers
    print(even_number[5]) # printing the index of thr even number

except ZeroDivisionError:# handle error form dividing by zero
    print("cannot divide by zero")
except IndexError:# handle error form out of index 
    print("Out of range")
finally:
    print("this execute always")

# IndentationError: unindent does not match any outer indentation level  #if level of function is left and right from the original line

