"""Kevin Hinds"""

MINIMUM_LENGTH = 6

password = input("Please enter password of at least {} length: ".format(MINIMUM_LENGTH))
while len(password) < MINIMUM_LENGTH:
    password = input("Please enter password of at least {} length: ".format(MINIMUM_LENGTH))
print('*' * len(password))


