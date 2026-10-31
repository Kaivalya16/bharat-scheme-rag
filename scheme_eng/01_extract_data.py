import pandas as pd, glob
df = pd.read_csv(glob.glob("scheme_eng/*.csv")[0])
print(df.shape)
print(df.columns.tolist())
print(df.iloc[0].to_dict())