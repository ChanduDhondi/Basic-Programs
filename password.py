import secrets
import string

alphabet = string.ascii_letters

pwd = ''
for i in range(0,10):
    pwd += "".join(secrets.choice(alphabet))

print(pwd)