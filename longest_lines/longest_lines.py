# https://www.codeeval.com/open_challenges/2/

import sys

#list: [abcd, ab..]
def longest_lines(list, line):
	current_line_length = len(line)
	updated_list = []
	if (len(list) == 0):
		updated_list.append(line)
		return updated_list
	i = 0
	while (i < len(list)):
		if (current_line_length >= len(list[i])):
			updated_list.append(line)
			updated_list += (list[i:])
			return updated_list
		else:
			updated_list.append(list[i])
		i = i + 1
	updated_list.append(line)
	return updated_list

#long_lines = []
#long_lines = longest_lines(dummy_list, 'abcdeabcde')
#long_lines = longest_lines(dummy_list, 'abcabc')
#long_lines = longest_lines(dummy_list, 'abcdabcd')
#long_lines = longest_lines(dummy_list, 'abc')

def read_input(file):
	input_file = open(sys.argv[1], 'r')
	return input_file.read().split('\n')

def main():
	long_lines = []
	for line in read_input(sys.argv[1]):
		long_lines = longest_lines(long_lines, line)
	print long_lines

main()
		
	

	