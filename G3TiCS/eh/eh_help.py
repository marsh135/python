import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Data - chess_games_cleaned_20000.csv")

# Get all of the Move_ columns
move_columns = [col for col in df.columns if col.startswith("Move_")]

# Count how many individual player moves (plies) occurred
df["Ply_Count"] = df[move_columns].notna().sum(axis=1)

# Convert plies into normal chess move numbers
df["Move_Count"] = (df["Ply_Count"] + 1) // 2

# Find mean game length for each first move
mean_moves = df.groupby("Move_1")["Move_Count"].mean()

# Sort from shortest to longest average game
mean_moves = mean_moves.sort_values()

# Create bar chart
plt.figure(figsize=(12, 6))

plt.bar(mean_moves.index, mean_moves.values)

plt.xlabel("First Move")
plt.ylabel("Mean Number of Moves")
plt.title("Mean Game Length by First Move")

#plt.xticks(rotation=45)
plt.tight_layout()

plt.show()