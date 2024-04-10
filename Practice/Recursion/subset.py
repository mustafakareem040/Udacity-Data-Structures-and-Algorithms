def _subset(arr, length, index, content, result):
	if index == length:
		if content not in result:
			result.append(content)
		return result

	_subset(arr, length, index+1, content, result)
	_subset(arr, length, index+1, content + [arr[index]], result)
	return result
def subset(arr):
	return _subset(arr, len(arr), 0, [], [])

print(subset([9, 8, 9, 8]))

