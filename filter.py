nums = [1,2,3,4,5,6,7,8,9,10]

# def filterFunction(num):
#     if num%2 == 0: 
#         return num

evenNums = list(filter(lambda num : (num%2) == 0,nums))

num = [num for num in nums if num%2 == 0]
print (evenNums)

