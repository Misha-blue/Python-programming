import os
import tempfile
import uuid


class File:

    def __init__(self, path):
        self.path = path
        self.current_position = 0

    def __str__(self):
        return '{}'.format(self.path)

    def write(self, content):
        with open(self.path, "w") as f:
            return f.write(content)

    def read(self):
        with open(self.path, "r") as f:
            return f.read()

    def __add__(self, other):
        new_path = os.path.join(tempfile.gettempdir(), str(uuid.uuid4().hex))
        new_file = type(self)(new_path)
        new_file.write(self.read() + other.read())
        return new_file

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.path) as f:
            f.seek(self.current_position)
            current_line = f.readline()
            if not current_line:
                self.current_position = 0
                raise StopIteration("EOF")
            self.current_position = f.tell()
            return current_line


obj1 = File('read_example')
obj2 = File("example")
print(obj1)
print(obj2)
print(obj1 + obj2)
for line in File('read_example'):
    print(line)
