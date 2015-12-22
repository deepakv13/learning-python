#https://www.codeeval.com/open_challenges/8/

import sys

def reverse(input):
	if(len(input) <= 1):
		return input
	if (len(input) == 2):
		return input[1] + input[0]
	return input[len(input)-1] + reverse(input[1:-1]) + input[0]

def reverse_sentence(sentence):
	reversed_sentence = reverse(sentence)
	reversed_words = reversed_sentence.split()
	output = ''
	for word in reversed_words:
		output += ' ' + reverse(word)
	return output[1:]

#print reverse(sys.argv[1])

print reverse_sentence(sys.argv[1])