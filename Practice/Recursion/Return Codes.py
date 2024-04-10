from math import log10
def get_character(num):
	return chr(96 + num)

def _return_codes(num, left, result, builder, l, w):
	if left:
		builder += get_character(left)
	if l >= 2:
		_return_codes(num % w, num // w, result, builder, l - 1, w // 10)
		w //= 10
		r = num // w
		if r <= 26:
			_return_codes(num % w, r, result, builder, l - 2, w // 10)
	elif l == 0:
		result.append(builder)
	else:
		_return_codes(None, num, result, builder, 0, 0)
	return result

def return_codes(num):
	l = int(log10(num))
	w = 10**l
	return _return_codes(num, None, [], "", l+1, w)

print(return_codes(25))