def print_integers(n):
	if n <= 1:
		print(n)
		return
	print(n)
	return print_integers(n-1)

print_integers(4)