import argparse
import string
import random


class Generator:

    def __init__(self):
        self.number = int(1000)
        self.filename = 'test.bin'


    def _generate_string(self):
        str_len = 4
        return ''.join([random.choice(string.ascii_letters) for i in range(str_len)]) + '\n'

    def generate_file(self):
        with open(self.filename, 'w') as f:
            for i in range(self.number):
                f.write(self._generate_string())


Generator().generate_file()