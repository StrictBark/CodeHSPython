# update the function to return `word` with all instances of `letter` removed!
def remove_all_from_string(word, letter):
    while letter in word:
        x=word.find(letter)
        if x == -1:
            continue
        else:
            word = word[:x] + word[x+1:]
    return word
    
print(remove_all_from_string("hello", "l"))
