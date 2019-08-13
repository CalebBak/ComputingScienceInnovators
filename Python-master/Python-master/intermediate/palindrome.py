"""
File: Palindrome.py
Name:
    
Python program that detects whether 
the given word is a palindrome or not.
Concepts covered: Strings, loops, slicing, if/else
"""
def main():
    word = input("Enter a word ")
    print("%s is %s a palindrome" % (word, "" if isPalindrome(word) else "not"))
    
def isPalindrome(word):
    # Remove whitespace
    word = ''.join(word.split())
    
    return word == word[::-1]

if __name__ == "__main__":
    main()
