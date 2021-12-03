import itertools
import random
import string
import hashlib
import time

#start timer and init length
time_start = time.time()
length = 1
chars = "ABCDEFGHIJKLMOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*."
#read the file line by line
f = open("hashes.txt","r")
read_lines1 = f.read()
#set pass length to 8 or less
while length <= 8:
    password = random.choices(chars, k=length)
#generate possible guesses
    password2 = "".join(password)
    hashGuess = hashlib.md5(password2.encode()).hexdigest()
#check if the guess matches print time and say this is the password
    if hashGuess in read_lines1:
        print(time.time() - time_start)
        print("This is " + password2)
        length = length + 1

    # else:
    #     password = random.choices(chars, k=length)
    #     password2 = "".join(password)
    #     hashGuess = hashlib.md5(password2.encode()).hexdigest()



# for line in read_lines1:
#     hashGuess = ""
#     print (line)
#     while hashGuess != line:
#         password = random.choices(chars,k=length)
#         password2 = "".join(password)
#         hashGuess = hashlib.md5(password2.encode()).hexdigest()
#
#         if hashGuess == line:
#             print (time.time()-time_start)
#             print ("This is "+ password2)
#             length = length + 1
#
#         else:
#             password = random.choices(chars, k=length)
#             password2 = "".join(password)
#             hashGuess = hashlib.md5(password2.encode()).hexdigest()
#
#
#
