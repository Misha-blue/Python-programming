import pandas as pd


class Test:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_df(cls, allel_id):
        df = pd.DataFrame({allel_id: [0], 'x': [1], 'y': [3]})
        return cls(df["x"].item(),
                   df["y"].item())


class Te:
    def a(self, s):
        return pd.DataFrame({s: [0], 'x': [1], 'y': [3]})

    def __init__(self, s):
        df = self.a(s)
        self.x = df['x'].item()
        self.y = df['y'].item()


string = "a"
print(Test.from_df(string).__dict__)
print(Te(string).__dict__)
