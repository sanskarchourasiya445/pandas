# Column selection
df['team1']
df[['team1','team2']]

# Row selection
df.iloc[0]
df.loc[0]

# Slicing
df.iloc[0:5]

# Boolean filtering
df[df['first_ings_score'] > 180]

# Multiple conditions
df[(df['team1']=='Chennai') & (df['team2']=='Mumbai')]
