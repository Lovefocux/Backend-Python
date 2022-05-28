# Check if a word is an anagrams
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True



def find_anagrams(first_word, second_word):
 # [assignment] Add your code here.
    first_word = input("Enter first word:")
    second_word = input("Enter first word:")

    if(sorted(first_word) == sorted(second_word)):
        print ("True")
    else:
        print ("False")

find_anagrams("tools", "stool")