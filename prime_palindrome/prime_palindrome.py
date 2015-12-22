def is_palindrome(input):
    if (len(input) <= 1):
        return True
    else:
        #print "comparing %r" %input
    	return (input[0] ==  input[-1]) and is_palindrome(input[1:-1])
	
#print is_palindrome("AA")

def is_prime(n):
	if (n<=1):
		return False
	elif (n<=3):
		return True
	i = 2
	while (i * i <= n):
		if (n%i == 0):
			return False
		i = i + 1
	return True

#print is_prime(929)

def is_prime_palindrome(value):
	return is_palindrome(str(value)) and is_prime(value)


def get_max_prime_palindrome(num):
	i = num
	while (i > 1):
		#print "Checking for: %r" %i
		if (is_prime_palindrome(i) == True):
			return i
		i = i - 1
	return None

print get_max_prime_palindrome(1000)
