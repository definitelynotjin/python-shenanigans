import string
import random

characters = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.choice(characters) for i in range(9))
print("random pass is", password)
