"""Write a program that checks if two given strings are anagrams of each other (contain the same characters in a 
    different order). The program should ignore spaces and case."""
string = "act"
string2 = "caat"

def anagram_checker(string1,string2):
    is_anagram=True
    for i in set(string1):
        if not i in set(string2):
            is_anagram=False
            break
    
    print(f" Given {string1} and {string2} are anagrams {is_anagram}")
    return is_anagram
check = anagram_checker(string1=string,string2=string2)
# $$ important points missed using collections.counter
# $$ missed to check the word frequency which is imp in anagramchecker.
# efficient way 
#   Counter creates the frequency of elements either string or list into a dictionary
# example: banana --> {'b':1,'a':3,'n':2}
from collections import Counter
def Anagram_checker(string1,string2):
    is_anagram = Counter(string1)==Counter(string2)
    if is_anagram:
        print(f"anagram words")
    else:
        print(f"not a anagram")
    return is_anagram
print(Anagram_checker(string1=string,string2=string2))