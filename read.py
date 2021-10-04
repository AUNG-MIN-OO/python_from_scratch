file = open('./text.txt')

for line in file:
    print(line)

# file.seek(0)

# lineList = file.readlines()
# print(lineList)

file.seek(50)
paragraph = file.read(100)
print(paragraph)