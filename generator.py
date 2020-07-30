import math
import random
import json
import string
import time

#  C:/Users/littlebeantheboss/Desktop/Pygame/Email Generator/names.txt.json
#  C:/Users/littlebeantheboss/Desktop/Pygame/Email Generator/surnames.txt.json
#  C:/Users/littlebeantheboss/Desktop/Pygame/Email Generator/passwords.txt.json
#  C:/Users/littlebeantheboss/Desktop/Pygame/Email Generator/randomwords.txt.json

g = input("JSON first name list path: ")
h = input("JSON surname list path: ")
i = input("JSON password list path: ")
j = input("JSON random word list path: ")

chars = string.ascii_letters + string.digits + '!@#$%&*()^'
uchars = string.digits
firstname = json.loads(open(g).read())
surname = json.loads(open(h).read())
keyss = json.loads(open(i).read())
wordslist = json.loads(open(j).read())

startTime = int(time.time() * 1000)

first = []
last = []
passwords = []
usernames = []
words = []
domains = ['@gmail.com', '@yahoo.com', '@comcast.net', '@live.com', '@aol.com', '@hotmail.com', '@msn.com', "@outlook.com", "gmail"]

for i in firstname:
    first.append(i)

for i in surname:
    last.append(i)

for i in keyss:
    passwords.append(i)

for i in wordslist:
    words.append(i)

def generation():
#generate passwords
    a = 0
    if a == 0:
        while True:
            if a == 1000:
                break
             #chooses 1 of 3 options
            generate = random.random() * 3
            # two random choices of the index
            createpass1 = math.floor(random.random() * 1000)
            createpass2 = math.floor(random.random() * 1000)
            #random number of characters at the end of a password
            rangevalue = math.floor(random.random() * 8)
            randomstring = "".join(random.choice(chars) for i in range(rangevalue))
            if generate <= 1:
                password = first[createpass1] + last[createpass2] + randomstring
                passwords.append(password.lower())
            elif generate <= 2:
                password = passwords[createpass1] + randomstring
                passwords.append(password.lower())
            elif generate <= 3:
                password = randomstring
                passwords.append(password)
            a += 1

        print(passwords)

    b = 0
    if b == 0:
        while True:
            if b == 10000:
                break
            generate = random.random() * 8
            # two random choices of the index
            create1 = math.floor(random.random() * 1000)
            create2 = math.floor(random.random() * 1000)
            create3 = math.floor(random.random() * 8)
            rangevalue = math.floor(random.random() * 8)
            randomstring = "".join(random.choice(uchars) for i in range(rangevalue))
            if generate <= 1:
                username = first[create1] + last[create2] + domains[create3]
                usernames.append(username.lower())
            elif generate <= 2:
                username = first[create1] + last[create2] + randomstring + domains[create3]
                usernames.append(username.lower())
            elif generate <= 3:
                username = last[create2] + randomstring + domains[create3]
                usernames.append(username.lower())
            elif generate <= 4:
                username = first[create1][0] + last[create2] + randomstring + domains[create3]
                usernames.append(username.lower())
            elif generate <= 5:
                username = words[create1] + words[create2] + randomstring + domains[create3]
                usernames.append(username.lower())
            elif generate <= 6:
                username = first[create1] + words[create2] + domains[create3]
                usernames.append(username.lower())
            elif generate <= 7:
                username = first[create1] + words[create2] + randomstring + domains[create3]
                usernames.append(username.lower())
            elif generate <= 8:
                username = words[create1] + words[create2] + domains[create3]
                usernames.append(username.lower())
            b += 1
        endTime = int(round(time.time()) * 1000)
        ellapsed = endTime - startTime
        print(usernames)
        print("Generated ", b, " usernames and ", a, ' passwords in ', ellapsed, '  milliseconds.')

generation()


