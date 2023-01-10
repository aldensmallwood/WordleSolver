guess = ""
feedback = ""
green_letters = []


my_file = open("wordlist.txt", "r")

data = my_file.read()

word_list = data.split("\n")
my_file.close()

print(word_list)


print("good starter words are: stare, tried, splice, crane... but start with whatever you want")

for guesses in range(6):  # iterating through each guess
    guess = input("\nword: ").lower()  # making sure the input is only in lower case
    print("g - green, y - yellow, w - wrong / grey")
    feedback = input("Feedback ").lower()
    if feedback == "ggggg":
        print("WELL DONE!! Guess ", guesses + 1)
        break
    # this is the bulk of getting rid of irrelevant words below

    temp_tuple = tuple(word_list)
    for word in temp_tuple:  # You can't iterate over a list you want to change, so using a tuple.
        for i in range(5):  # running through each letter in feedback, comparing its significance to every 5 letter word
            if feedback[i] == "g":  # creating list of all letters in solution to help double letter issue
                green_letters.append(guess[i])
            if feedback[i] == "w" and guess[i] in word:  # if letter is wrong and this letter is in a word in list
                if guess.count(guess[i]) > 1 and feedback[guess.find(guess[i])] == 'y':  # if there was a yellow letter
                    # before the grey letter, do not remove word
                    break
                elif guess[i] in green_letters:  # if the letter is in the green letter list do not remove word
                    break
                else:  # else remove it
                    word_list.remove(word)
                break
            elif feedback[i] == "g" and guess[i] != word[i]:  # if letter is green, and it isn't in the word, remove it
                word_list.remove(word)
                break
            elif feedback[i] == "y" and guess[i] not in word:  # if letter is yellow, and it isn't in word, remove it
                word_list.remove(word)
                break
            elif feedback[i] == "y" and guess[i] == word[i]:  # if letter is yellow, and it is in same spot, remove it
                word_list.remove(word)
                break
    print("The wordle can be ... ", word_list)

