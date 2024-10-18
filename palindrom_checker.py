"""Write a program that checks if a given string is a palindrome (reads the same forwards and backwards). 
    The program should ignore spaces, punctuation, and case."""

# string = input("enter the string to check palindrome")
string1 = "Gfg, is best : for ! Geeks ;"
string= "Hello, World!"
string2 = "A man, a plan, a canal, Panama!"
def palindrome_checker(string):
    pure_string = "".join(filter(lambda x:x.isalpha() or x.isdigit() or x.isspace(),string.lower()))
    pure_string = pure_string.replace(" ","")
    print(pure_string)
    print(len(pure_string))
    print(len(pure_string)//2)
    j=None
    for i in range(len(pure_string)//2):
        if pure_string[i]!=pure_string[-(i+1)]:
            j =1
            break
    if j:print(f"{string} not a palindrome")
    else:print(f"{string} is a palindrome")
palindrome_checker(string=string)
palindrome_checker(string=string1)
palindrome_checker(string=string2)   

#efficient way 

def Palindrome_checker(string):
    pure_string = "".join(filter(str.isalnum,string.lower()))
    if pure_string[:]==pure_string[::-1]:
        print(f"{string} is a palindrome")
    else:
        print(f"{string} is not a palindrome")
Palindrome_checker(string=string)
Palindrome_checker(string=string1)
Palindrome_checker(string=string2)


