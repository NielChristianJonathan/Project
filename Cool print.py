import time
alph = [chr(i) for i in range(65,123)]
alph.append(" ")
char = [""]
word = input("Enter your word: ")

next = True
for i in word:
    if next:
        next = False
        for j in range(len(alph)):
            print("".join(char),end="")
            print(alph[j])
            time.sleep(0.01)
            if alph[j] == i:
                char.append(alph[j])
                next = True
                break
    else:
        print("You enter an unusual character (don't enter a number)")
        break

    
