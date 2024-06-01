import os

# creating File
a = open("myfile.txt", "a")

#Write file
a.write("This is File Handling.")

#Close the file
a.close()

#Read a file
a = open("myfile.txt", "r")
print(a.read())

#Delete a File
os.remove("myfile.txt")