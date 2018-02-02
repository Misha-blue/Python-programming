import argparse


class FileReader:

    def __init__(self, filepath):
        self.filepath = filepath

    def read(self):
        try:
            with open(self.filepath) as f:
                data = f.read().replace('\n', '')
                return data
        except OSError:
            return ""


def main():
    filepath = get_arguments()
    reader = FileReader(filepath)
    print(reader.read())


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath")
    result = parser.parse_args()
    return result.filepath


if __name__ == "__main__":
    main()
