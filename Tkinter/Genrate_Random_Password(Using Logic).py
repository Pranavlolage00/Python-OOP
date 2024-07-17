import random
a = 0
password = ''
while a < 8:
    if random.randint(0, 61) < 10:
        password += chr(random.randint(48, 57))
    elif 10<random.randint(0, 61)<36:
        password += chr(random.randint(65, 90))
    else:
        password += chr(random.randint(97, 122))
    a += 1
print(password)
