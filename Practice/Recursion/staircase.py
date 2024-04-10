def staircase(num):
	"""
    :param: n - number of steps in the staircase
    Return number of possible ways in which you can climb the staircase
    """
	c = 0
	if num > 0:
		c += staircase(num - 1)
	else:
		return 1
	if num > 1:
		c += staircase(num - 2)
	if num > 2:
		c += staircase(num - 3)
	return c

if __name__ == '__main__':
	print(staircase(7)) # 44
	print(staircase(3)) # 4 