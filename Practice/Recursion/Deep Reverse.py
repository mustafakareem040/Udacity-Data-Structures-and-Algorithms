def _deep_reverse(array, result, length, index):
	if index == -1 or not array:
		return result
	element = array[index]
	if isinstance(element, (list, tuple)):
		new = _deep_reverse(element, [], len(element), len(element)-1)
		result.append(new)
	else:
		result.append(element)
	return _deep_reverse(array, result, length, index-1)

def deep_reverse(array):
	return _deep_reverse(array, [], len(array), len(array)-1)

if __name__ == '__main__':
	arr1 = [1, [2, 3, [4, [5, 6]]]]
	arr2 = [1, [2,3], 4, [5,6]]
	arr3 = [1, 2, 3, 4, 5]
	print(deep_reverse(arr1) == [[[[6, 5], 4], 3, 2], 1])
	print(deep_reverse(arr2) == [ [6,5], 4, [3, 2], 1])
	print(deep_reverse(arr3) == [5, 4, 3, 2, 1])