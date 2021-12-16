import pandas as pd
import smogn

#Loading data
print('Loading data')
df = pd.read_csv('IllustrisTNG.csv')
df = df.sample(frac = 1, random_state = 42)
df = df.reset_index(drop=True)

print('SMOGNing data')
#Let's do the code by itself choose the best regions
df_s = smogn.smoter(data = df_1, y = "stellar_mass")

print('Writting data')
df_s.to_csv('stellar_mass-smoogn_data.csv')

print('SMOGN is finished!')
