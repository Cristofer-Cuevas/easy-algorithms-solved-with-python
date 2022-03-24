# O(log n) 
#  Most operations in this algorithm runs in O(1)
def binary_search(numbers, target):
	first = 0
	last = len(numbers) - 1

	while first <= last:
		mid_point = (first + last) // 2
		if numbers[mid_point] == target: 
			return print('Was value found?:', True)
		elif numbers[mid_point] < target:
			first = mid_point - 1
		else:
			last = mid_point + 1


numbers = [x for x in range(1, 11)]

# print(numbers)

binary_search(numbers, 5)


# Recursive implementation
def recursive_binary_search(numbers, target):
	# O(1)
	if len(numbers) == 0:	return print('Was recursive binary search result value found?:', False)

	mid_point = (len(numbers)) // 2
	# O(log n)
	if numbers[mid_point] == target:
		return print('Was recursive binary search result value found?:', True)
	else: 
		if numbers[mid_point] < target:
			recursive_binary_search(numbers[mid_point+1:], target)
		elif numbers[mid_point] > target: 
			recursive_binary_search(numbers[:mid_point], target)

recursive_binary_search(numbers, 11)