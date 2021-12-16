import pandas as pd
import smogn

print("Loading data")
#Loading data
df = pd.read_csv('IllustrisTNG.csv')
df = df.sample(frac = 1, random_state = 42)
df = df.reset_index(drop=True)

#Choosing the regions to work
rg_mtrx = [
    [0.06, 1, 1],  ## over-sample ("minority")
    [0.32, 0, 1],  ## under-sample ("majority")
    [0.7, 1, 1],  ## over-sample ("minority")
    [1.0, 1, 1],  ## over-sample ("minority")
    [2.1, 0, 1],  ## under-sample ("majority")
]

print("SMOGing data")
df_s = smogn.smoter(
    ## main arguments
    data = df_1,           ## pandas dataframe
    y = 'radius_g',          ## string ('header name')
    k = 7,                    ## positive integer (k < n)
    pert = 0.04,              ## real number (0 < R < 1)
    samp_method = 'balance',  ## string ('balance' or 'extreme')
    drop_na_col = True,       ## boolean (True or False)
    drop_na_row = True,       ## boolean (True or False)
    replace = False,          ## boolean (True or False)

    ## phi relevance arguments
    rel_thres = 0.3,#0.1,         ## real number (0 < R < 1)
    rel_method = 'manual',    ## string ('auto' or 'manual')
    rel_ctrl_pts_rg = rg_mtrx ## 2d array (format: [x, y])
)

print('Writting data')
df_s.to_csv('radius-smoogn_data.csv')

print('SMOGN is finished!')
