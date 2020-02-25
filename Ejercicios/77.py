def cantidad(n):
	if n<=9:
		return 1
	return 1+cantidad(n/10)