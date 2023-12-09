from random import choices
from string import ascii_letters, digits

characters = ascii_letters + digits + ',._'

def generate_password(length):
    return ''.join(choices(characters, k=length))

print(generate_password(10))
print(generate_password(10))
