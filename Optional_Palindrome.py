"""
Determine if a word is a palindrome.
"""

def is_palindrome(word):
    palindrome=""
    for i in range(1,len(word)+1):
        palindrome += word[-i]
        # print(palindrome)
    print(palindrome == word)
is_palindrome("word")

#BONUS : For a given input string S, return the longest palindrome found within.
#If multiple substrings qualify, print them all in the same order as they appear in S.

def longest_palindrome(sentence):
    pass


def main():
    pass

if __name__ == "__main__":
    main()
