import string, random

print("".join(random.choice(string.ascii_uppercase + '9') for i in range(81)))




