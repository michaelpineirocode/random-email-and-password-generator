import json

#takes input
g = input("File path and name: ")
x = input("Object Name: ")

#splits up the terms and gets file name
h = str(g).split("/")
i = len(h) - 1
filename = h[i]

#gets the content from the txt document as is
rawcontent = open(g, "r")
words = rawcontent.read()
rawcontent.close()

#this splits the list into one long line and then splits into individual words
contwords = words.replace("\r", "").replace('\n', ' ')
split = contwords.split(" ")

#formats each item in the list
for i in range(len(split)):
    if i < len(split) - 1:
        split[i] = '    "' + split[i] + '",'
    else:
        split[i] = '    "' + split[i] + '"'

#adds an enter after each line
finalArray = "\n".join(split)
#formats to json format and stores as a dictionary. It then executes the code in the string
format = 'dict1 ={' + "\n" + '"' + str(x) + '": [' + "\n" + finalArray + "\n" + "]" + "\n" + "}"
exec(format)

#creates/writes to a new json file of the same name
out_file = open(filename + ".json", "w")
json.dump(dict1, out_file)
out_file.close()