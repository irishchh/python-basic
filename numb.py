# with function
def number():
    n = int(input("Enter a number of rows"))# input from the user
    for i in range(n):# for print the range user wants
        for f in range(1,i + 2):#
            print(i+1, end=(" ")) #space after every number
        print()
number()



# n = int(input("Enter a number of rows"))# input from the user
# for i in range(n):# for print the range user wants
#     for f in range(1,i + 2):#
#         print(i+1, end=(" ")) #space after every number
#     print()

# result
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# 6 6 6 6 6 6



# n = int(input("Enter a number of rows"))# input from the user
# for i in range(n):# for print the range user wants(this for function indicate the column)
#     for f in range(1,i + 2):# this for function inticates the row 
#         print(f+1, end=(" ")) #space after every number(add number by one)
#     print()

# result
# 2
# 2 3
# 2 3 4
# 2 3 4 5