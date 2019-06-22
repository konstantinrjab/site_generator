import random
import string


class StringGenerator:
    def get(self, length):
        letters = string.ascii_lowercase

        return ''.join(random.choice(letters) for letter in range(length))
