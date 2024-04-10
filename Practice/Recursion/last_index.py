def last_index(arr, target):
	if len(arr) == 0:
		return -1
	if arr[-1] == target:
		return len(arr)-1

	return last_index(arr[:-1], target)

print(last_index([1, 2, 5, 5, 4], 1))
print(last_index([1, 4, 3, 2, 1], 2))
print(last_index([1, 1, 1], 2))