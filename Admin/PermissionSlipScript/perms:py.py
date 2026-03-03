import pandas as pd
import glob
import os

# -----------------------------
# SETTINGS
# -----------------------------
INPUT_FOLDER = "python/Admin/PermissionSlipScript/csvs"
NAME_COLUMN = "Student Name"
APPROVED_COLUMN = "Approved"
OUTPUT_FILE = os.path.join(INPUT_FOLDER, "permission_master.xlsx")

def main():

    files = glob.glob(os.path.join(INPUT_FOLDER, "*.csv"))

    if not files:
        print("No CSV files found.")
        return

    all_students = set()
    per_file_completed = {}

    for file in files:
        df = pd.read_csv(file)

        if NAME_COLUMN not in df.columns:
            raise ValueError(f"{file} missing '{NAME_COLUMN}' column")

        if APPROVED_COLUMN not in df.columns:
            raise ValueError(f"{file} missing '{APPROVED_COLUMN}' column")

        # Keep only rows that are actually approved
        completed = df[df[APPROVED_COLUMN].astype(str).str.strip().str.lower() == "yes"]

        names = (
            completed[NAME_COLUMN]
            .astype(str)
            .str.strip()
        )

        label = os.path.splitext(os.path.basename(file))[0]

        completed_set = set(names)

        per_file_completed[label] = completed_set
        all_students.update(completed_set)

    # Build master table
    all_students = sorted(all_students)

    master = pd.DataFrame({
        "Student Name": all_students
    })

    # One column per file
    for label, completed_set in per_file_completed.items():
        master[label] = master["Student Name"].isin(completed_set)

    # Write Excel
    with pd.ExcelWriter(OUTPUT_FILE, engine="openpyxl") as writer:
        master.to_excel(writer, index=False, sheet_name="Permissions")

    print(f"Created {OUTPUT_FILE}")


if __name__ == "__main__":
    main()