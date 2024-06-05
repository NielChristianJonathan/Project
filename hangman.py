import random

character_dict ={}
stickman = ["____\n    |\n    O","____\n    |\n    O\n   /","____\n    |\n    O\n   /|","____\n    |\n    O\n   /|\ ","____\n    |\n    O\n   /|\ \n    |","____\n    |\n    O\n   /|\ \n    |\n   /","____\n    |\n    O\n   /|\ \n    |\n   / \ "]
character_dict["computer"] = ["It's a technology","It's popular in this era","This is a tool commonly used for work and play","This tool can be connected to the internet", "This tool has components like a monitor, keyboard, and mouse", "It can be used to run various programs or applications","It is widely used in offices, schools, and homes"]
character_dict["elephant"] = ["It's an animal","It is a herbivore","This animal is often found in Africa and Asia","This animal is known for its large size and strength","It is one of the largest land animals on Earth","This animal is known for its high intelligence and social behavior","It has a long trunk and large ears"]
character_dict["dictionary"] = ["Books","This book is used to find meanings of words","It contains words arranged alphabetically","Often used by students and writers","It provides definitions, pronunciations, and sometimes translations","It is a reference book found in libraries and schools","It can be either printed or available online"]


def choose_char_easy():
    global character_dict
    character_dict = {}
    counter = 0
    n = int(input("How many char do you want to play: "))
    while counter < n:
        char = input("Enter your character\n")
        char.lower()
        if char not in character_dict:
            counter += 1
            character_dict[char] = []
            print("Enter 7 question about your character")
            for i in range(7):
                quest = input(f"{i+1}. ")
                character_dict[char].append(quest)
        else:
            print("You've input that character, try another character")
    return character_dict

def choose_char_hard():
    global character_dict
    character_dict = {}
    counter = 0
    n = int(input("How many char do you want to play: "))
    while counter < n:
        char = input("Enter your character\n")
        char.lower()
        if char not in character_dict:
            counter += 1
            character_dict[char] = []
            quest = input("Enter question about your character\n")
            character_dict[char].append(quest)
        else:
            print("You've input that character, try another character")
    return character_dict

def hangman_easy(word):
    guess_char = []
    guessed = ["_ "]*len(word)
    counter = 0
    while counter < len(stickman):
        print("="*50)
        print(" "*((50-len("Guess your character"))//2),end="")
        print("Guess your character")
        print("="*50)
        true = False
        for j in range(counter+1):
            print(j+1,".",character_dict[word][j]) 
        for j in guessed:
            print(j,end="")
        print()
        guess = input("Guess the alphabet: ")
        if guess != "":
            guess = guess[0].lower()
            if guess not in guess_char:
                guess_char.append(guess)
                for d in range(len(word)):
                    if guess == word[d]:
                        guessed[d] = guess+" "
                        true = True
                if not true:
                    print("#"*50)
                    print(" "*((50-len("you're wrong !!!")-2)//2),end="")
                    print("You're wrong !!!")
                    print("#"*50)
                    print("-"*((49-len("HANGMAN"))//2),end=" ")
                    print("HANGMAN",end=" ")
                    print("-"*((49-len("HANGMAN"))//2))
                    print(stickman[counter])
                    print()
                    counter += 1
                    if counter == 7:
                        print("You Lose the game")
                        print(f"The character is {word}")
            else:
                print("You've guessed this char")
            if "_ " not in guessed:
                print("="*50)
                print(" "*((50-len("Congratsss you win"))//2),end="")
                print("Congratsss you win")
                print("="*50)
                break
        else:
            print("Please enter an alphabet")

def hangman_hard(word):
    guess_char = []
    guessed = ["_ "]*len(word)
    counter = 0
    while counter < len(stickman):
        print("="*50)
        print(" "*((50-len("Guess your character"))//2),end="")
        print("Guess your character")
        print("="*50)
        true = False
        print(character_dict[word][0])
        for j in guessed:
            print(j,end="")
        print()
        guess = input("Guess the alphabet: ")
        if guess != "":
            guess = guess[0].lower()
            if guess not in guess_char:
                guess_char.append(guess)
                for d in range(len(word)):
                    if word[d] == guess:
                        guessed[d] = guess+" "
                        true = True
                if not true:
                    print("#"*50)
                    print(" "*((50-len("you're wrong !!!")-2)//2),end="")
                    print("You're wrong !!!")
                    print("#"*50)
                    print("-"*((49-len("HANGMAN"))//2),end=" ")
                    print("HANGMAN",end=" ")
                    print("-"*((49-len("HANGMAN"))//2))
                    print(stickman[counter])
                    print()
                    counter += 1
                    if counter == 7:
                        print("You Lose the game")
                        print(f"The character is {word}")
            else:
                print("You've guessed this char")
            if "_ " not in guessed:
                print("Congratsss you win")
                break
        else:
            print("Please enter an alphabet")

def main():
    while True:
        print("Welcome to the Hangman game")
        print("1. Easy")
        print("2. Hard")
        print("3. Custom game")
        print("0. Exit")
        choose = input("Choose your game: ")
        if choose == "1":
            character_dict = {}
            character_dict["computer"] = ["It's a technology","It's popular in this era","This is a tool commonly used for work and play","This tool can be connected to the internet", "This tool has components like a monitor, keyboard, and mouse", "It can be used to run various programs or applications","It is widely used in offices, schools, and homes"]
            character_dict["elephant"] = ["It's an animal","It is a herbivore","This animal is often found in Africa and Asia","This animal is known for its large size and strength","It is one of the largest land animals on Earth","This animal is known for its high intelligence and social behavior","It has a long trunk and large ears"]
            character_dict["dictionary"] = ["Books","This book is used to find meanings of words","It contains words arranged alphabetically","Often used by students and writers","It provides definitions, pronunciations, and sometimes translations","It is a reference book found in libraries and schools","It can be either printed or available online"]
            for key in character_dict.keys():
                hangman_easy(key)
                print("\nEnter 0 if you want to exit\nPress any char to the next question")
                a = input("Your choice: ")
                if a == "0":
                    break
                else:
                    pass
        elif choose == "2":
            character_dict = {}
            character_dict["computer"] = ["It's a technology","It's popular in this era","This is a tool commonly used for work and play","This tool can be connected to the internet", "This tool has components like a monitor, keyboard, and mouse", "It can be used to run various programs or applications","It is widely used in offices, schools, and homes"]
            character_dict["elephant"] = ["It's an animal","It is a herbivore","This animal is often found in Africa and Asia","This animal is known for its large size and strength","It is one of the largest land animals on Earth","This animal is known for its high intelligence and social behavior","It has a long trunk and large ears"]
            character_dict["dictionary"] = ["Books","This book is used to find meanings of words","It contains words arranged alphabetically","Often used by students and writers","It provides definitions, pronunciations, and sometimes translations","It is a reference book found in libraries and schools","It can be either printed or available online"]
            for key in character_dict.keys():
                hangman_hard(key)
                print("press 0 to exit\nPress any key to next question")
                a = input("Your choice: ")
                if a == "0":
                    break
                else:
                    pass
        elif choose == "3":
            while True:
                print("Custom Game")
                print("1. Easy\n2. Hard\n0. Exit")
                difficult = input("Choose your difficult: ")
                if difficult == "1":
                    custom_dict = choose_char_easy()
                    print(custom_dict)
                    for key in custom_dict.keys():
                        hangman_easy(key)
                elif difficult == "2":
                    custom_dict = choose_char_hard()
                    
                    for key in custom_dict.keys():
                        hangman_hard(key)
                elif difficult == "0":
                    break

        elif choose == "0":
            print("="*50)
            print(" "*((50-len("Thank you"))//2),end="")
            print("THANK YOU")
            print("="*50)
            break


main()