guess = ""
feedback = ""

word_list = ['hello', 'enter', 'hulls', 'happy', 'crate', 'salve', 'store', 'evens']

print("good starter words are: stare, tried, splice, crane... but start with whatever you want")

for guesses in range(6):
    guess = input("\nword: ").lower()  # making sure the input is only in lower case
    print("g - green, y - yellow, w - wrong / grey")
    feedback = input("Feedback ").lower()
    if feedback == "ggggg":
        print("WELL DONE!! Guess ", guesses + 1)
        break
    # this is the bulk of getting rid of irrelevant words below

    temp_tuple = tuple(word_list)
    for word in temp_tuple:  # You can't iterate over a list you want to change, so using a tuple.
        for i in range(5):
            if feedback[i] == "w" and guess[i] in word:
                if guess.count(guess[i]) > 1 and feedback[guess.find(guess[i])] == 'y':
                    break
                else:
                    word_list.remove(word)
                break
            elif feedback[i] == "g" and guess[i] != word[i]:
                word_list.remove(word)
                break
            elif feedback[i] == "y" and guess[i] not in word:
                word_list.remove(word)
                break
            elif feedback[i] == "y" and guess[i] == word[i]:
                word_list.remove(word)
                break
    print("The wordle can be ... ", word_list)

