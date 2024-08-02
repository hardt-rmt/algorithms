# O(nlog(n)) time | O(1) space
def two_number_sum_s1(arr, target_sum):
	arr.sort()
	left = 0
	right = len(arr) - 1
	while left < right:
		current_sum = arr[left] + arr[right]
		if current_sum == target_sum:
			return [arr[left], arr[right]]
		elif current_sum < target_sum:
			left += 1
		elif current_sum > target_sum:
			right -= 1
	return []


# O(n) time | O(n) space
def two_number_sum_s2(arr, target_sum):
	nums = {}
	for num in arr:
		potential_match = target_sum - num
		if potential_match in nums:
			return [potential_match, num]
		else:
			nums[num] = True
	return []


# O(n ^ 2) time | O(1) space
def two_number_sum_s3(arr, target_sum):
	for i in range(len(arr)):
		for j in range(i + 1, len(arr)):
			if arr[i] + arr[j] == target_sum:
				return [arr[i], arr[j]]
	return []


array = [3, 4, -4, 8, 11, 1, -1, 6]
targetSum = 10
print(two_number_sum_s1(array, targetSum))
print(two_number_sum_s2(array, targetSum))
print(two_number_sum_s3(array, targetSum))