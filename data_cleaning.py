import pandas as pd

# Load IPL data
df = pd.read_csv('ipl_2022.csv')

print("Original Data Shape:", df.shape)
print()

# 1. Check for missing values
print("Missing Values:")
print(df.isnull().sum())
print()

# Handle missing values
# Fill missing numeric with mean
if 'margin' in df.columns:
    df['margin'] = df['margin'].fillna(df['margin'].mean())

# Fill missing text with 'Unknown'
df['toss_decision'] = df['toss_decision'].fillna('Unknown')
print("After filling missing values")
print()

# Drop rows with too many missing values
df_clean = df.dropna(thresh=15)
print("After dropping rows:", df_clean.shape)
print()

# 2. Remove duplicates
print("Duplicates before:", df_clean.duplicated().sum())
df_clean = df_clean.drop_duplicates()
print("Duplicates after:", df_clean.duplicated().sum())
print()

# 3. Data type conversion
# Convert scores to integers
if 'first_ings_score' in df_clean.columns:
    df_clean['first_ings_score'] = df_clean['first_ings_score'].astype(int)
    df_clean['second_ings_score'] = df_clean['second_ings_score'].astype(int)

print("Data types after conversion:")
print(df_clean.dtypes.head())
print()

# 4. String operations
# Make team names uppercase
df_clean['team1'] = df_clean['team1'].str.upper()
df_clean['team2'] = df_clean['team2'].str.upper()

# Replace city names
df_clean['venue'] = df_clean['venue'].str.replace('Mumbai', 'MUM')
df_clean['venue'] = df_clean['venue'].str.replace('Pune', 'PUN')

# Check for specific teams
delhi_matches = df_clean[df_clean['team1'].str.contains('DELHI') | df_clean['team2'].str.contains('DELHI')]
print("Delhi team matches:", len(delhi_matches))
print()

# 5. Date parsing
df_clean['date_parsed'] = pd.to_datetime(df_clean['date'], errors='coerce')
print("Date column converted to datetime")
print("Earliest match:", df_clean['date_parsed'].min())
print("Latest match:", df_clean['date_parsed'].max())
print()
print("Final Cleaned Data Shape:", df_clean.shape)
