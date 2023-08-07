# num = int(input("Enter a number"))
# prime = True
# for i in range(2,num):
#     if (num % i == 0 and num !=2):
#         prime = False
#         break
# if prime:
#     print("The number you entered is prime")
# else:
#     print("The number you entered is odd")

# while True:
#     for i in range(0,10):
#         print(i)
#     break

# num = int(input("Enter a number"))
# factorial = 1
# for i in range(1,num+1):
#     factorial = factorial*i
# print(f"The factorial of {num} this number is {factorial}")

# n = 3
# for i in range(3):
#     print("*" * (i+1))
# n = 3
# for i in range(3):
#     print(" " * (n-1-i), end="")
#     print("*" * (2*1+i), end="")
#     print(" " * (n-1-i))


# n = 3
# for i in range(3):
#     print("*" * (i+1),end="")

# num = int(input("Enter a number"))
# for i in range(1,11):
#     print(f"{num}X{i}={num*i}")


# user = input("Enter your name")
# def fun1():
#     print(f"{user} good day")

# fun1()


# def great(name):
#     gr = 'hello ' + name
#     return gr
# a = great("Irish")

# great('name')

# factorial(n) = n*factorial(n-1)

# def factorial(i):
#     if i == 0 or i == 1:
#         return i
#     else:
#         return n*factorial(n-1)

# def check_even_odd(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"

# # Taking input from user
# num = int(input("Enter a number: "))

# result = check_even_odd(num)
# print(f"The number {num} is {result}.")

# def sum_of_natural_numbers(n):
#     if n == 1:
#         return 1
#     else:
#         return n + sum_of_natural_numbers(n-1)

# # Test the function
# n = 5
# result = sum_of_natural_numbers(n)
# print(f"The sum of the first {n} natural numbers is: {result}")


# n = 3
# for i in range(3):
#     print("*" * (n-i))

# def inches_to_cm(inches):
#     cm = inches * 2.54
#     return cm

# # Test the function
# inches = float(input("Enter the length in inches: "))
# centimeters = inches_to_cm(inches)
# print(f"{inches} inches is equal to {centimeters} centimeters.")

# def remove_and_strip_words(input_list, word_to_remove):
#     output_list = [item.strip() for item in input_list if item.strip() != word_to_remove.strip()]
#     return output_list

# # Test the function
# words_list = ["  apple ", "banana ", " orange", "pear ", "banana"]
# word_to_remove = "banana"

# result_list = remove_and_strip_words(words_list, word_to_remove)
# print("Original list:", words_list)
# print("List after removing and stripping the word:", result_list)

# class QuizQuestion:
#     def __init__(self, question, options, correct_option):
#         self.question = question
#         self.options = options
#         self.correct_option = correct_option

#     def check_answer(self, user_answer):
#         return user_answer.lower() == self.correct_option.lower()


# def run_quiz(questions):
#     score = 0
#     total_questions = len(questions)

#     for i, question in enumerate(questions, start=1):
#         print(f"Question {i}: {question.question}")
#         for j, option in enumerate(question.options, start=1):
#             print(f"{j}. {option}")

#         user_choice = int(input("Enter your answer (1, 2, 3, 4): "))
#         if 1 <= user_choice <= 4:
#             if question.check_answer(question.options[user_choice - 1]):
#                 print("Correct!\n")
#                 score += 1
#             else:
#                 print(f"Wrong! The correct answer is {question.correct_option}\n")
#         else:
#             print("Invalid choice. Please enter a valid option.\n")

#     print(f"Quiz completed! Your score: {score}/{total_questions}")


# if __name__ == "__main__":
#     # Define your quiz questions here
#     questions = [
#         QuizQuestion("What is the capital of France?", ["London", "Berlin", "Paris", "Madrid"], "Paris"),
#         QuizQuestion("Which planet is known as the 'Red Planet'?", ["Venus", "Mars", "Jupiter", "Saturn"], "Mars"),
#         QuizQuestion("What is the largest mammal in the world?", ["Elephant", "Blue Whale", "Giraffe", "Lion"], "Blue Whale"),
#     ]

#     run_quiz(questions)


# def multiplication_table(number, length):
#     for i in range(1, length + 1):
#         result = number * i
#         print(f"{number} * {i} = {result}")

# # Test the function
# num = int(input("Enter the number for which you want to generate the multiplication table: "))
# table_length = int(input("Enter the length of the multiplication table: "))

# multiplication_table(num, table_length)

