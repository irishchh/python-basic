# def add(x, y):
#     return x + y

# def subtract(x, y):
#     return x - y

# def multiply(x, y):
#     return x * y

# def divide(x, y):
#     if y == 0:
#         return "Error: Cannot divide by zero!"
#     return x / y

# def calculator():
#     print("Welcome to the Simple Calculator App!")
#     print("Available operations:")
#     print("1. Add (+)")
#     print("2. Subtract (-)")
#     print("3. Multiply (*)")
#     print("4. Divide (/)")
#     print("5. Exit")

#     while True:
#         choice = input("Enter the operation number (1/2/3/4/5): ")

#         if choice == '5':
#             print("Thank you for using the calculator. Goodbye!")
#             break

#         if choice not in ('1', '2', '3', '4'):
#             print("Invalid choice. Please select a valid operation.")
#             continue

#         num1 = float(input("Enter the first number: "))
#         num2 = float(input("Enter the second number: "))

#         if choice == '1':
#             print("Result:", add(num1, num2))
#         elif choice == '2':
#             print("Result:", subtract(num1, num2))
#         elif choice == '3':
#             print("Result:", multiply(num1, num2))
#         elif choice == '4':
#             print("Result:", divide(num1, num2))

# if __name__ == "__main__":
#     calculator()



# import random
# import string

# def generate_password(length=12):
#     characters = string.ascii_letters + string.digits + string.punctuation
#     password = ''.join(random.choice(characters) for _ in range(length))
#     return password

# def main():
#     print("Welcome to the Random Password Generator!")
#     length = int(input("Enter the length of the password (default is 12): "))

#     if length < 1:
#         print("Invalid password length. Using default length (12).")
#         length = 12

#     password = generate_password(length)
#     print("Your random password is:", password)

# if __name__ == "__main__":
#     main()