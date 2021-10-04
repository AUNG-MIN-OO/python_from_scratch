# prices = [1000,2000,3000,4000,5000]

# # double_prices = []
# # for price in prices : 
# #     double_prices.append(price*2)

# double_prices = [price*2 for price in prices]
# print (double_prices)

nums = [1,2,3,4,5,6,7,8,9,10]
# even_doubleNums = []
# for num in nums : 
#     if num%2 == 0: 
#         even_doubleNums.append(num*2)
# print(even_doubleNums)
even_doubleNums = [num*2 for num in nums if num%2 == 0]
print(even_doubleNums)
