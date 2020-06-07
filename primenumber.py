def is_prime(n):
	for j in range(2, (n+1)):
		if(n%j == 0):
			if(n == 2):
				return True
			else:
				return False
		else:
			if(j == (n-1)):
				return True
			else:
				pass

def prime_number_list(length):
		result = []
		i = 2
		while True:
			if(is_prime(i) == True):
				result.append(i)
			if(result.__len__() == length):
				break
			i = i + 1
		return result

length = int(input('Length? '))
print(prime_number_list(length))