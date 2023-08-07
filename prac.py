# def monkey_trouble(a_smile, b_smile):
#   if a_smile and b_smile:
#     return True
#   if not a_smile and not b_smile:
#     return True
#   return False

# while True:
#     print("[1,2,3,4,5]")
#     b = input("Enter a number to see index of the numbers in the list")
#     if b =='1':
#         print("1 is in index 0")
#     elif b =='2':
#         print("2 is in index 1")
#     elif b =='3':
#         print("3 is in index 2")
#     elif b =='4':
#         print("4 is in index 3")
#     elif b =='5':
#         print("5 is in index 4")
#     else:
#         print("The number you Entered is not in range")
#     break


# def searh(num):
#     list = [5,7,2,9,3]
#     for i,n in enumerate(list):
#         if num == n:
#             return i
# print(searh(a))


# print("OPTION are [5,7,2,9,3]")
# def alt(num):
    
#     list = [5,7,2,9,3]
#     for i in range(len(list)):
#         if num == list[i]:
#             return i
        

# a = int(input("Enter the item :"))

# print(alt(a))

import random

def avg(num):
    lst = []
    for i in range(num):
        lst.append(random.radint(1,100))
    print(lst)

    avg = 0
    for n in lst:
        sum += n

    average = sum /len(lst)
    return average

a = int(input("Enter the item :"))
print(avg(a))



