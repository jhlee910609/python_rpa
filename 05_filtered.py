import pandas as pd

df = pd.read_json("mando.json")
print(df.count())