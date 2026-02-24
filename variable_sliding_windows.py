

s = "abcdabcdefbb" # len = 12
seen = set()
left = 0
max_len = 0

for right in range(len(s)):
    print("right = ", right)
    while s[right] in seen:
        print("s[right] = ",s[right] , ", seen =",seen)
        seen.remove(s[left])
        print(" after removing s[left] =  ",s[left] , "seen = ", seen)
        left += 1

    seen.add(s[right])
    max_len = max(max_len, right - left + 1)

print(max_len)
