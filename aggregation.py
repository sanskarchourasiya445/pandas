import pandas as pd

df = pd.read_csv('IPL.csv')

print("=== GROUPBY OPERATIONS ===")

# 1. Simple groupby - count matches
print("\n1. Total matches won by each team:")
wins_count = df.groupby('match_winner').size()
print(wins_count)
print()

# 2. Groupby with single column stats
print("\n2. First innings score statistics by winner:")
first_innings_stats = df.groupby('match_winner')['first_ings_score'].agg(['sum', 'mean', 'max', 'min', 'count'])
print(first_innings_stats)
print()

# 3. Groupby with multiple columns
print("\n3. Both innings scores by winner:")
both_innings = df.groupby('match_winner')[['first_ings_score', 'second_ings_score']].mean()
print(both_innings)
print()

# 4. Multiple aggregations
print("\n4. Detailed match stats by team:")
team_stats = df.groupby('match_winner').agg({
    'first_ings_score': ['sum', 'mean', 'max'],
    'second_ings_score': ['sum', 'mean', 'max'],
    'margin': ['mean', 'max', 'min'],
    'match_id': 'count'  # number of wins
})
print(team_stats)
print()

# 5. Stage-wise analysis
print("\n5. Stage-wise team performance:")
stage_stats = df.groupby(['stage', 'match_winner']).agg({
    'first_ings_score': 'mean',
    'second_ings_score': 'mean',
    'match_id': 'count'
})
print(stage_stats)
print()

# 6. Multiple groupby keys
print("\n6. Toss winner vs match winner:")
toss_match = df.groupby(['toss_winner', 'match_winner']).size()
print(toss_match.head(10))
print()

print("\n=== BASIC AGGREGATION FUNCTIONS ===")

# Direct column aggregations
print("\nOverall Tournament Statistics:")
print("Total first innings runs:", df['first_ings_score'].sum())
print("Average first innings score:", round(df['first_ings_score'].mean(), 2))
print("Highest first innings:", df['first_ings_score'].max())
print("Lowest first innings:", df['first_ings_score'].min())
print("Total matches played:", df['first_ings_score'].count())
print()

print("Margin Statistics:")
print("Average winning margin:", round(df['margin'].mean(), 2))
print("Biggest win margin:", df['margin'].max())
print("Smallest win margin:", df['margin'].min())
print()

print("Top Performers:")
max_score = df['highscore'].max()
player_max = df[df['highscore'] == max_score]['top_scorer'].iloc[0]
print(f"Highest individual score: {max_score} by {player_max}")
print()

# Multiple aggregations at once
print("Summary of all numeric columns:")
numeric_cols = ['first_ings_score', 'second_ings_score', 'margin', 'highscore']
print(df[numeric_cols].agg(['sum', 'mean', 'max', 'min', 'count']))
