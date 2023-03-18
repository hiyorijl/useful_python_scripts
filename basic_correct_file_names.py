import os
import re

#asking for the targeted directory
target_dir = input("Please input the targeted directory: ")

#changing the current working directory
os.chdir(target_dir)

#listing the files in the directory
files = os.listdir()

#looping through the files
for file in files:
    parts = file.split(".")
    name = parts[0]
    words = name.split("_")
    new_name = ""
    #looping through the words
    for word in words:
        word = word.capitalize()
        word = word.rstrip("1234567890")
        new_name += word + "_"
    new_name = new_name[:-1]
    new_name += "." + parts[1]
    os.rename(file, new_name)

#printing a message
print("The files have been renamed successfully >u<!")
