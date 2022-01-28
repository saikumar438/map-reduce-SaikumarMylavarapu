from anyio import open_file


openFile = open("outputFile.txt","r")  # open file, read-only
sorted_file = open("sortedOutput.txt", "w") # open file, write
lines = openFile.readlines()
lines.sort()

for line in lines:
 sorted_file.write(line)

openFile.close()
sorted_file.close()