# 3.4 Practical Example 
# Here’s an example of reading from one file and writing to another: 
with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    for line in infile:
        outfile.write(line)
        print("reading from one file and writing to another file is succesfull")