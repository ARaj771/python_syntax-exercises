
def print_upper_words(words):
    """Prints all the words in a list in uppercase letters."""
    
    for word in words:
        print(word.upper())








def print_upper_words_e(words):
    """Takes the words in the list that start with e or E and changes all the letters to uppercase in that word"""

    for word in words:
       if(word[0] == 'e' or word[0] == 'E'):
           print(word.upper())
        
        
def print_upper_words_char(words,char):
    """ Takes a list of words and characters and changes all letters in the word to uppercase if the word begins with one of the characters in the list of characters."""
    
    for word in words:
        for ch in char:
            if(word[0]== ch):
                print(word.upper())