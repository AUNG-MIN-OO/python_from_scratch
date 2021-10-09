# with open('./text.txt','w') as file:
#     file.write()


# with open('./text.txt','a') as file:
#     file.write()

lists = ['I am Aung Min Oo','\nI am pro']

with open('./text.txt','a') as file:
    file.writelines(lists)