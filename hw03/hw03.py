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

if (platform == 'Windows'):  # FOR NON-LINUX USERS
    url = "http://raw.githubusercontent.com/eneko/data-repository/master/data/words.txt"
    import os
    from urllib.request import urlopen
    wordfile = urlopen(url)
    words = wordfile.read().decode('utf-8').upper().split()
else:  # FOR LINUX USERS
    wordfile = open("/usr/share/dict/words")
    words = wordfile.read().upper().split()


def all_steps(w):
    one_step_words = []
    for word in words:
        if (len(w) + 1 == len(word)):
            # check letters
            temp_word = word
            for i in range(len(w)):
                if w[i] in temp_word:
                    temp_word = temp_word.replace(w[i], '', 1)
                else:
                    break
            if (len(temp_word) == 1):
                one_step_words.append(word)
    print(one_step_words)


if __name__ == "__main__":
    step_continue = "y"
    while (step_continue == "y"):
        word = input("Please enter your word: ")
        all_steps(word.upper())
        step_continue = input("Enter 'y' to continue: ")
