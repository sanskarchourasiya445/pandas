# Apply function
df['score_category'] = df['first_ings_score'].apply(
    lambda x: 'High' if x>180 else 'Low'
)

# String ops
df['venue'] = df['venue'].str.upper()
