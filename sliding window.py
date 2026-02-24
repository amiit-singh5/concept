
# find maximum sum of 3 elements using sliding window.
# very good example of sliding windows. 
# Time complexity → O(n)
nums = [2, 1 , 5, 1, 3, 2]
k = 3

window_sum = sum(nums[:k]) # sum till 0,1,2
print("window_sum : ", window_sum)
max_sum = window_sum

for i in range(k, len(nums)): # start k =3, i = 3,4,5
    #print(nums[i],"i = ", i, "i - k = ",i - k) # i= 3 ,4,5
    window_sum += nums[i]        # add next elementR.D. Sharma
    print("window_sum 1 : ", window_sum)
    window_sum -= nums[i - k]    # i-k = 0,1,2 ,remove element leaving window
    print("window_sum 2 : ", window_sum)
    max_sum = max(max_sum, window_sum)

print(max_sum)