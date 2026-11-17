import pandas as pd

# Load the original CSV
file_path = "G2APCSP/survey.csv"
df = pd.read_csv(file_path, dtype=str)  # read everything as string

# Wrap each value in quotes
df_single_quoted = df.applymap(lambda x: f"'{x}'" if pd.notna(x) else "''")

# Save the new CSV
output_path = "G2APCSP/survey_strings.csv"
df_single_quoted.to_csv(output_path, index=False)

print(f"✅ All items wrapped in quotes. Saved to: {output_path}")