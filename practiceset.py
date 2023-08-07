# num1 = int(input("Enter a random number"))
# num2 = int(input("Enter a random number"))
# num3 = int(input("Enter a random number"))
# num4 = int(input("Enter a random number"))

# if num1>num4:
#     f1 = num1
# else:
#     f1 = num4

# if num2>num3:
#     f2 = num2
# else:
#     f2 = num3

# if (f1>f2):
#     print(str(f1) + "is greater in the list")
# else:
#     print(str(f2) + "is greater in the list")

Eng = int(input("Enter the percentage"))
Nep = int(input("Enter the percentage"))
math = int(input("Enter the percentage"))

if (Eng<33 or Nep<33 or math<33):
    print("You have less than 33% in one of the sub")
elif(Eng+Nep+math)/3 <40:
    print("You failed the exam")
else:
    print("you have passed the exam")