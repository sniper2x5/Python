
def palindrome (word):
    """palindrome(word) - returns true if the words is a palindrome and false otherwise"""
    return word.lower().replace(" ","")==word.lower().replace(" ","")[::-1]
print palindrome("Yo banana boy")

