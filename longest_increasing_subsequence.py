def LIS(nums):
	n = len(nums)
	longest = [1]*n
	for i in range(0, n):
		for j in range(0, i):
			if nums[i] > nums[j] and longest[i] < longest[j] + 1:
				longest[i] = longest[j] + 1
	return longest
	
arr = [6, 2, 5, 1, 7, 4, 8, 3]
res = LIS(arr)
print(res)
