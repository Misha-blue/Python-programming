class PascalList:
    def __init__(self, original_list=None):
        self.contener = original_list or []

    def __getitem__(self, index):
        return self.contener[index-1]

    def __setitem__(self, index, value):
        self.contener[index - 1] = value

    def __str__(self):
        return self.contener.__str__()
