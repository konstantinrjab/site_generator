import random
import string


class StringGenerator:
    def get_random_string(self, length=10):
        letters = string.ascii_lowercase

        return ''.join(random.choice(letters) for letter in range(length))
