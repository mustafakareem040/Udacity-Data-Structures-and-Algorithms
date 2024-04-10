# Fourth of Recursion problems

def reverse_string(string: str, index = 0) -> str:
	"""Return reversed input string

	Examples:
	reverse_string("abc") returns "cba"

	Args:
	input(str): string to be reversed

	Returns:
	a string that is the reverse of input"""
	if len(string) <= 1 or index >= len(string)//2:
	  	return string
	new_string = string[:index] + string[-index-1] + string[index+1:-index-1] + string[index] + string[len(string)-index:]
	return reverse_string(new_string, index + 1)


if __name__ == '__main__':
	# Test cases
	print(reverse_string('Hello')) # olleH
	print(reverse_string('ab')) # ba
	print(reverse_string('abc')) # cba
	print(reverse_string('Life is not difficult')) # tluciffid ton si efiL