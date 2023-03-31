# Programming Challenge 3
# by Randy Hucker and Sam Graler


# We addressed the issue of speed in this program by making sure that we only traverse the list
# of words a single time. Our code looks at the words in the list, and if the length is greater
# than our word of interest by 1, we know that it could be a one-step word. Any 1 letter can be
# added, so there is no need to keep track of which specific letter we're checking for.

# From there, we start to check the letters. If the first letter from our word of interest
# appears in the word from the dictionary, we remove it and proceed to the next letter. If the
# first letter doesn't exist, the word from the dictionary cannot be a one-step word, so we break
# out of that iteration and proceed to the next word.

# This prevents us from checking words that cannot be one-step words, AND from checking more
# characters than necessary when we realize our word can no longer be a one-step word. This makes
# our solution quick and efficient, especially since we traverse the large dictionary only once


from sys import platform

# if on Linux OS, use built in dictionary (contains more words) (we coded using a Linux OS)

if (platform == 'win32'):  # FOR NON-LINUX USERS
    url = "http://raw.githubusercontent.com/eneko/data-repository/master/data/words.txt"
    import os
    from urllib.request import urlopen
    wordfile = urlopen(url)
    words = wordfile.read().decode('utf-8').upper().split()
else:  # FOR LINUX USERS
    wordfile = open("/usr/share/dict/words")
    words = wordfile.read().upper().split()


def sort_words():
    longestWordLength = len(max(words, key=len))
    sorted_array = []
    for x in range(1, longestWordLength+1):
        result = [textword for textword in words if len(textword) == x]
        sorted_array.append(sorted(result))
    return sorted_array


sorted_array = sort_words()
longest_ladder_dict = {}


def all_steps(w):
    one_step_words = []
    for word in sorted_array[len(w)]:
        # check letters
        temp_word = word
        for i in range(len(w)):
            if w[i] in temp_word:
                temp_word = temp_word.replace(w[i], '', 1)
            else:
                break
        if (len(temp_word) == 1):
            one_step_words.append(word)
    return one_step_words


def longest_ladder(numletters):
    for word in sorted_array[numletters-1]:
        all_steps_result = all_steps(word)
        updated = False
        # for target in sorted_array[numletters]:
        for target in all_steps_result:
           # if target in all_steps_result:
            # Make Connection
            try:
                set_val = 1 + longest_ladder_dict[target][0]
                val_array = longest_ladder_dict[target][1]
                val_array.append(word)
                longest_ladder_dict[word] = [set_val, val_array]
                updated = True
            except:
                longest_ladder_dict[word] = [2, [target, word]]
                updated = True
            # try:
            #     if (updated == False and longest_ladder_dict[target]):
            #         longest_ladder_dict.pop(target)
            # except:
            #     continue
    print("----------------")
    print(f"The {numletters} length words finsihed.")
    print("----------------")
    if (numletters == 1):
        return
    longest_ladder(numletters-1)
    return


if __name__ == "__main__":
    step_continue = "y"
    while (step_continue == "y"):
        input_choice = input("Please enter 1 for word, 2 for longest ladder: ")
        if (input_choice == "1"):
            word = input("Please enter your word: ")
            print(all_steps(word.upper()))
        elif (input_choice == "2"):
            longest_ladder(27)

            max_value = max(longest_ladder_dict,
                            key=lambda key: longest_ladder_dict[key])
            print(
                f"The Longest Word Ladder is {longest_ladder_dict[max_value][0]} words long.")
            print(
                f"The word {longest_ladder_dict[max_value][1][-1]} builds the ladder:")
            wordlen = 0
            for word in longest_ladder_dict[max_value][1][::-1]:
                if len(word) > wordlen:
                    wordlen = len(word)
                    print(word)

        step_continue = input("Enter 'y' to continue: ")
