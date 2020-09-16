import pandas as pd


df = pd.read_csv('/home/yassine/embedding-projector-standalone/oss_data/all_categories_10k.csv')

df.to_csv('/home/yassine/embedding-projector-standalone/oss_data/all_categories_10k.tsv', sep='\t', index=False, header=False)


print(len(df))

