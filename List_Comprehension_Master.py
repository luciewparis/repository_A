""" 
A couple of exercises to become fluent with list comprehensions
"""
'''
# TODO: Find all of the numbers from 1-1000 that are divisible by 7
exo_1 = [number for number in range(1001) if number % 7 == 0]
print("EXO 1 - divisible by 7 : ")
print(exo_1)

# TODO: Find all of the numbers from 1-1000 that have a 3 in them
exo_2 = [number for number in range(1001) if str(number).find("3") != -1]
print("EXO 2 - has a 3 : ")
print(exo_2)

# TODO: Count the number of spaces in a string
string_ = input("enter a string : \n")
string_count = string_.count(" ")
print("EXO 3 - nb of spaces = "+str(string_count))

# print teststring.count(' ')  
#  
# # TODO: normally you would just do this, but for the practice....

# TODO: Remove all of the vowels in a string [make a list of the non-vowels]
vowels=['a', 'e', 'i', 'o', 'u']
string_no_vowel = [char for char in string_ if char not in vowels]
print("EXO 4 - without vowels : "+"".join(string_no_vowel))

# TODO: Find all of the words in a string that are less than 4 letters
words = string_.split()
less_than_four = [word for word in words if len(word)<4]
print(f"EXO 5 - less than 4 letters : {less_than_four}")

# TODO: Use a dictionary comprehension to count the length of each word in a sentence.
dico = {(k,v) for (k,v) in zip(words, (len(word) for word in words))}
print(f"EXO 6 - dico = {dico}")

# TODO: Use a nested list comprehension to find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9) (ie non prime numbers)
list_nb_div = [nb for nb in range(1,1001) if nb % 2 == 0 or nb % 3 == 0 or nb % 5 == 0 or nb % 7 == 0 ]
#print(f"EXO 7 - list div = {list_nb_div}")

# comprehension testing truth for divisibility: [True for divisor in range(2,10) if number % divisor == 0]
list_nb_div2 = [nb for nb in range(1,1001) if [True for divisor in range(2,10) if nb % divisor == 0 ]]
#print(f"EXO 7 - list div (version avec range) = {list_div2}")


Check qu'on a le même résultat (réponse: oui)
result = (list_nb_div == list_nb_div2)
print("diff entre les 2 résultats de l'exo 7? "+ str(result))

# TODO: For all the numbers 1-1000, use a nested list/dictionary comprehension to find the highest single digit each number is divisible by.

#version sans comprehension
maxi_div = []
for nb in list_nb_div:
    divisors_nb = []
    for divisor in range(2,10):
        if nb % divisor == 0:
            divisors_nb.append(divisor)
    maxi_div.append(max(divisors_nb))

dico_div = {(k,v) for (k,v) in zip(list_nb_div, maxi_div)}

#version avec comprehension (mettre les arguments des append() en elements de list comprehension)

dico_div2 = {(k,v) for (k,v) in zip(list_nb_div,
                                    [max([
                                        divisor for divisor in range(2,10) if nb % divisor == 0
                                    ]) 
                                     for nb in list_nb_div]
                                    )}


Tentative 2 (brouillon)
dico_div = {(k,v) for (k,v) in zip(list_nb_div,
                                   [max([
                                        divisor for divisor in range(2,10) if [True for nb in list_nb_div if nb % divisor == 0]])]
                                    )}
Tentative 1 (brouillon)
dico_div = {(k,v) for (k,v) in zip(list_div, 
                                   [max(div) for div in [divisor for divisor in range(1,10) if nb % divisor ==0]]
                                   )}

print(f"EXO 8 - dico avec highest div = {dico_div2}")
'''


# List comprehension for providing a list of all of the numbers a number is divisible by: divisor_list:
number = 100
divisor_list = [divisor for divisor in range(1,number) if number % divisor == 0 ]
print(divisor_list)


# SOLUTION: [divisor for divisor in range(1,1001) if number % divisor == 0]

