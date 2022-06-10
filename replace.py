# Read in the file
with open('example.txt', 'r') as file:
    filedata = file.read()

# Replace the target string
filedata = filedata.replace('placement', 'screening')

# Write the file out again
with open('example.txt', 'w') as file:
    file.write(filedata)
