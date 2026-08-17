# write apython program to print the contents of a directory using the os module search online for the function which does that

import os

# Specify the directory path
path = "D:/"

# Get the list of files and folders
contents = os.listdir(path)

# Print each item
for item in contents:
    print(item)