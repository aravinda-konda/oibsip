import random
import string

length=int(input('Enter password length : '))
print('Enter Character type(letters,numbers,symbols) : ')
char_types=list(input().split())
listt=''

for char_type in char_types:
    if char_type=='letters':
        listt+=string.ascii_letters
    elif char_type=='numbers':
        listt+=string.digits
    elif char_type=='symbols':
        listt+=string.punctuation
    

password=''
if listt:
    for i in range(length):
        char=random.choice(listt)
        password+=char
    print('Random generated Password : ',password,'\n')
else:
        print('Enter Character Type correctly')
