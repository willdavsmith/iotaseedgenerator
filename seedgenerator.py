import string, random

letters = string.ascii_uppercase + '9'

n = 81
output = ''
while (n != 0):
	output = output + random.choice(letters)
	n -= 1
print output




