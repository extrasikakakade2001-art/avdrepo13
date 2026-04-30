import pandas as pd

print("extract Data")

data = {
    'ID': [101, 102, 103],
    'Name': ['Ram', 'Raj', 'Raja'],
    'Age':[29, 34, 42]
}

df = pd.DataFrame(data)
print(df)