"""
Generate a password of the size given by a user.
"""
# requires 2 libraries
import random 
import string

size_user = int(input("Enter the size of your desired password"))
password_level = None #instead of {}

while password_level not in {"Y","N"}:
    password_level = input("Please enter Y if you need a strong password, N otherwise")

password_list = []
password = ""

'''
# IF version for a password with only numbers
if password_level == "N":
    # password_list.append(random.choice(string.ascii_letters,size_user-1)) marche pas avec un 2nd argument
    for i in range(size_user):
        #password_list.append(random.randint(0,9))
        password_list.append(random.choice(string.digits))
    password = "".join(str(p) for p in password_list)
# ELIF strong password
elif password_level == "Y": #version for a strong password i.e with letters, numbers, symbols
    for i in range(size_user):
        if random.randint(0,9)%2 == 0: # scenario 1: chiffre ou symbol
            if random.randint(0,9)%2 == 0:
                password_list.append(random.randint(0,9))
            else:
                password_list.append(random.choice('!$%&()*+,-.:;<=>?@[]^_`{|}~'))
        else: # scenario 2: nombre
            password_list.append(random.choice(string.ascii_letters))
    password = "".join(str(p) for p in password_list)
else:
    print("password level not defined!")
'''

''' solution optimizes the above by defining a list of ALL characters 
including numbers, letters and symbols
    chars = string.ascii_letters + string.digits + string.punctuation
then use
    password_list.append(random.choice(chars))
TRY IT OUT BY running code below and putting above tentative in ''' '''
    '''

if password_level == "N":
    # password_list.append(random.choice(string.ascii_letters,size_user-1)) marche pas avec un 2nd argument
    for i in range(size_user):
        #password_list.append(random.randint(0,9))
        password_list.append(random.choice(string.digits))
    password = "".join(str(p) for p in password_list)
# ELIF strong password
elif password_level == "Y": #version for a strong password i.e with letters, numbers, symbols
    for i in range(size_user):
        chars = string.ascii_letters + string.digits + string.punctuation
        password_list.append(random.choice(chars))
    password = "".join(str(p) for p in password_list)
else:
    print("password level not defined!")

print(password)