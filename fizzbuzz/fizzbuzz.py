#https://www.codeeval.com/open_challenges/1/submit/?lid=1267442

import sys


def get_test_cases():
        #test_cases = [[3, 5, 10],[2, 7, 15]]
        test_cases = open(sys.argv[1], 'r')
        return test_cases.read()
        #return test_cases
        
def main():
        test_file_content = get_test_cases()
	#print "Test File Content: %r" %test_file_content
	test_cases = test_file_content.split('\n')
	#print "Test cases: %r" %test_cases
        for test in test_cases:
		#print "Test: %r" %test
		if (not test == ' '):
			#print "This is test input: %r" %test
			test_arr = test.split()
			output = get_fizzbuzz_series(int(test_arr[0]), int(test_arr[1]), int(test_arr[2]))
			print output

def get_fizzbuzz_series(d1, d2, n):
    i = 1
    fizz_buzz_series = []
    while (i <= n):
        fb = fizzbuzz(i, d1, d2)
        fizz_buzz_series.append(fb)
        i = i + 1
    return fizz_buzz_series
        
            
def fizzbuzz(val, d1, d2):
    if (val % (d1 * d2) == 0):
        return 'FB'
    if (val % d1) == 0:
        return 'F'
    if (val % d2) == 0:
        return 'B'
    return val
    
#print get_test_cases()
            
main()

