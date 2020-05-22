'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# move left to right through the word.
# increment a counter if the 2 characters at "th"
# slice the word and return the count +count_th("sliced_word") (to hit the recursion requirement)

def count_th(word):
    # declare count
    count = 0
    sliced_word = word
    # Base Case
    # if there are no more characters to traverse
    if len(word) < 2:
        return 0
    # check if the first two indexes match th, 
    # if yes, increment count and slice the word
    elif word[0] + word[1] == "th":
        count += 1
        sliced_word = word[2:]
    # if they don't match check if the 2nd character is t and slice accordingly
    elif word[1] == "t":
        sliced_word = word[1:]
    # if the 2nd character does not equal "t" then we slice the first two characters from word
    else:
        sliced_word = word[2:]

    return count + count_th(sliced_word)



### Why is this a good case for recursion? Seems HIGHLY unnecessary and kinda hacky.....