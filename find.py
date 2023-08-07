# find how many 
# def anlayzer(sentence):
#     vowel = 0
#     spaces = 0
    
#     for char in sentence:
#         if (char == "a"or char =="e"or char =="i" or char =="o" or char == "u"):
#             vowel += 1

#         elif (char ==" "):
#             spaces += 1
        
#     consonent = len(sentence)-vowel-spaces
#     print(f"there are {consonent} connsonent total")
#     print(f"there are {vowel} vowel total")
#     print(F"there are {spaces} spaces total")
# def main():
#     sentence =input("Input the sentences:-\n")
#     anlayzer(sentence)

# if __name__== "__main__":
#     main()

def count_vowel_consonant_spaces(input_string):
    vowel = "AEIOUaeiou"