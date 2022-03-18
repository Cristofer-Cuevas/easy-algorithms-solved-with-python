# O(log n) 
#  Most operations in this algorithm runs in O(1)
def binary_search(numbers, target):
	first = 0
	last = len(numbers) - 1

	while first <= last:
		mid_point = (first + last) // 2
		if numbers[mid_point] == target: 
			return mid_point
		elif numbers[mid_point] < target:
			first = mid_point - 1
		else:
			last = mid_point + 1 


numbers = [x for x in range(1, 10)]

print(numbers)

print(binary_search(numbers, 5))


