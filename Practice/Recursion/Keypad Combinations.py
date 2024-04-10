from math import log10

keypad = {
	2: 'abc',
	3: 'def',
	4: 'ghi',
	5: 'jkl',
	6: 'mno',
	7: 'pqrs',
	8: 'tuv',
	9: 'wxyz'
	}

def _combine(num, builder, result, w):
	if num <= 0:
		result.append(builder)
		return result
	left = num // w
	for char in keypad[left]:
		_combine(num % w, builder + char, result, w // 10)
	return result


def get_characters(num):
	"""Given an integer `num`, find out all the possible strings that can be made using digits of input `num`. 
	Return these strings in a list. The order of strings in the list does not matter. However, as stated earlier, the order of letters in a particular string matters.
	
	Time Complexity:
	O(4^d)

	Space Complexity:
	O(4^d)
	where d is the digits length
	"""
	w = 10**(int(log10(num)))
	return _combine(num, "", [], w)


if __name__ == '__main__':
	print(get_characters(99))
	print(get_characters(354))