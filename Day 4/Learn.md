# File Handling in Python
python has many finction to creating, reading, updating and deleteing file.

# open()

The key function for working with files in Python is the open() function.
The open() function takes two parameters; filename, and mode.

There are four different methods (modes) for opening a file:

"r" - Read -    Default value. Opens a file for reading, error if the file does not exist
"a" - Append -  Opens a file for appending, creates the file if it does not exist
"w" - Write -   Opens a file for writing, creates the file if it does not exist
"x" - Create -  Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode

"t" - Text -    Default value. Text mode
"b" - Binary -  Binary mode (e.g. images)

# read()
The open() function returns a file object, which has a read() method for reading the content of the file
the read() method returns the whole text.

You can return one line by using the readline() method.

# Close()
It is a good practice to always close the file when you are done with it.

# Write file
To write to an existing file, you must add a parameter to the open() function:

"a" - Append - will append to the end of the file
"w" - Write - will overwrite any existing content

# Create file
To create a new file in Python, use the open() method, with one of the following parameters:

"x" - Create - will create a file, returns an error if the file exist
"a" - Append - will create a file if the specified file does not exist
"w" - Write - will create a file if the specified file does not exist

# Delete file
To delete a file, you must import the OS module, and run its os.remove() function.

# Delete Folder
To delete an entire folder, use the os.rmdir() method.


# Python with Django :

1. what is Django?
Django is a back-end server side web framework.
Django is free, open source and written in Python.
Django makes it easier to build web pages using Python.

2. How does Django Work?
Django follows the MVT design pattern (Model View Template).

3. Install Django 
pip install django

