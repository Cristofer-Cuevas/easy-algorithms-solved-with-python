def linear_search(list, target):
	# O(n) Linear runtime
	for i in range(0, len(list)):
	# O(1) Constant Time
		if list[i] == target:
			return i
	return None

numbers = [number for number in range(1, 10)]

print(numbers)

print(linear_search(numbers, 7))


# Recursive implementation
def recursive_linear_search(numbers, target, index):
	if numbers[index] == target:
		return index
	else:
		index += 1
		return recursive_linear_search(numbers, target, index)


print(recursive_linear_search(numbers, 7, index = 0))