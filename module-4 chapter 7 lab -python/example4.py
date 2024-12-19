# Example 4: Renaming a File 
import os

# Create a sample file to rename
with open('original_file.txt', 'w') as f:
    f.write('This file will be renamed.')

# Rename the file
os.rename('original_file.txt', 'renamed_file.txt')

print('File renamed from "original_file.txt" to "renamed_file.txt".')