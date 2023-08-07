import random
def choose_word():
    word_list = ["apple", "banana","graps","jack_fruit","orange"]
    return random.choice(word_list)

def display(word,guesses):
    display_word = ""
    for letter in word:
        if letter in guesses:
            display_word += letter
        else:
            display_word += "-"
    return display_word

def hangman():
    word = choose_word()
    guessed_letter = []
    attempts = 6
    print("welcome to hangman")

    while attempts > 0:
        print(display(word, guessed_letter))
        guess = input("guess the word")

        if len(guess) != 1 or not guess.isalpha():
            print("please enter a single letter.")
            continue

        if guess in guessed_letter:
            print("you've already guessed that word")
            continue


        guessed_letter.append(guess)

        if guess in word:
            print("correct")
            if display(word, guessed_letter) == word:
                print("congrats, you've won the game!")
                break
            else:
                attempts -= 1
                print("incorrect, you have", attempts, "attemps left.")

        if attempts == 0:
            print("sorry you've run out of attemps. the word", word)

hangman()



