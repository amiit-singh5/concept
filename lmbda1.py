# sum without sum and reduce from functools using list comprehesion
nums = [1,2,3,4]
total = 0
a = [total := total + x  for x in nums]

print(total)



# global temp 
# temp = nums[0]

# find max in nums = [1,2,3,4] using lambda

fun = lambda x : 
print([(lambda i, temp = nums[0]: (temp := i) if (i > temp) else temp)(i) for i in nums])