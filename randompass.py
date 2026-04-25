import random
import string

chars = string.ascii_letters + string.digits
password = "".join(random.sample(chars, 8))

print("Generated Password:", password)