import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def create_graph(dataset, name, bins):
    plt.hist(dataset, bins=bins, color='skyblue', edgecolor='black', zorder=2)
    plt.xlabel(f'{name} per Game')
    plt.ylabel('Frequency')
    plt.title(f'Distribution of {name}')
    plt.grid(True)
    plt.show()


df = pd.read_csv("data.csv")

length = df.shape[0]
threshold = 500 # threshold for line and scatter graphs
print(length)

# Print
print(df[['Turns', 'Wars']].corr())

df2 = df[["Turns", "Wars", "Starting Hand Difference"]]
print(df2.describe())

print(f"Longest War: {max(df['Longest War'].tolist())}")

# Graphs

# Scatter Plot/Bar graph
xs = []
ys = []
num_games = []

length = len(df)
max_diff = max(df['Starting Hand Difference'].max(), abs(df['Starting Hand Difference'].min()))

# Precompute which differences are common enough
diff_counts = df['Starting Hand Difference'].value_counts()
valid_diffs = diff_counts[diff_counts > threshold].index  # keep diffs with > threshold games

# Filter the main DataFrame once
filtered_df = df[df['Starting Hand Difference'].isin(valid_diffs)]

for t in range(0, max_diff + 6, 5):
    if t == 0:
        dfp1 = filtered_df[(filtered_df['Winner'] == 1) & (filtered_df['Starting Hand Difference'] > 0)].shape[0]
        dfp2 = filtered_df[(filtered_df['Winner'] == 2) & (filtered_df['Starting Hand Difference'] < 0)].shape[0]
        equal = filtered_df[filtered_df['Starting Hand Difference'] == 0].shape[0]
        total_games = filtered_df.shape[0]
    else:
        tier_df = filtered_df[filtered_df['Starting Hand Difference'].abs() >= t]
        dfp1 = tier_df[(tier_df['Winner'] == 1) & (tier_df['Starting Hand Difference'] > 0)].shape[0]
        dfp2 = tier_df[(tier_df['Winner'] == 2) & (tier_df['Starting Hand Difference'] < 0)].shape[0]
        total_games = tier_df.shape[0]

    if total_games == 0:
        continue

    xs.append(t)
    ys.append(round((dfp1 + dfp2) / total_games, 4) * 100)
    num_games.append(total_games)

plt.grid(True, zorder=0)
plt.scatter(xs, ys, color="darkblue", zorder=3)
plt.xlabel("Minimum Starting Hand Lead")
plt.ylabel("Win % with Stronger Hand")
plt.title(f"Filtered Win Rate vs Hand Difference (Freq > {threshold})")
plt.show()


# Line Graph
counts = df['Starting Hand Difference'].value_counts()
valid_diffs = counts[counts > threshold].index

filtered_df = df[df['Starting Hand Difference'].isin(valid_diffs)]
avg_lengths_filtered = filtered_df.groupby('Starting Hand Difference')['Turns'].mean()

plt.plot(avg_lengths_filtered.index, avg_lengths_filtered.values, color='darkblue')
plt.xlabel('Starting Hand Difference (Player 1 - Player 2)')
plt.ylabel('Average Game Length')
plt.title(f'Average Game Length vs Starting Hand Difference (Freq > {threshold})')
plt.grid(True)
plt.show()

# Histograms
create_graph(df['Turns'].tolist(), "Turns", 100)
create_graph(df['Wars'].tolist(), "Wars", 30)

