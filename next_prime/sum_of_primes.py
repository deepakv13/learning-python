#
import sys

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

#prime number follows the pattern of 6k+-1
def get_next_prime(p):
	if (p == 2):
		return 3
	if (p == 3):
		return 5
	k1 = (p - 1)/6.0
	k2 = (p + 1)/6.0
	k = None
	next_k = None
	next_d = None
	if (k1 == int(k1)):
		k = int(k1)
		next_d = -1
		next_k = k + 1
	else:
		k = int(k2)
		next_d = 1
		next_k = k
	next_p = ((6 * next_k) + next_d)
	if (is_prime(next_p)):
		#print "%r is prime" %next_p
		return next_p
	else:
		#print "%r is not prime" %next_p
		return get_next_prime(next_p)		

def get_sum_of_primes(count):
	counter = 1
	p = 2
	sum = 2
	while (counter < count):
		print "counter : %r, prime : %r" %(counter, p)
		p = get_next_prime(p)
		sum = sum + p
		counter = counter + 1
	return sum

print get_sum_of_primes(int(sys.argv[1]))
		
