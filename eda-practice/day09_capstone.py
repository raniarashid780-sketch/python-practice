# Dataset: Kaggle "Cafe Sales - Dirty Data for Cleaning Training" (dirty_cafe_sales.csv)
# https://www.kaggle.com/datasets/ahmedmohamed2003/cafe-sales-dirty-data-for-cleaning-training

from pathlib import Path
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Task 1: First look
# PREDICTION (write your own, in your words): which columns are messiest and why?
# Mark it "written after seeing the output" if you wrote it after running.
# ---------------------------------------------------------------------------
csv_path = Path(__file__).with_name("dirty_cafe_sales.csv")
df = pd.read_csv(csv_path)
raw = df.copy()                       # untouched copy, never modified

print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print("Data Types:")
print(df.dtypes)
print("Missing Values (isnull only - placeholders are NOT counted here):")
print(df.isnull().sum())
print("Duplicate rows:", df.duplicated().sum())
print("Unique Transaction IDs:", df["Transaction ID"].nunique(), "of", len(df))

# dropna=False so real NaN is visible next to the 'UNKNOWN'/'ERROR' placeholders
for col in ["Item", "Payment Method", "Location"]:
    print(df[col].value_counts(dropna=False))

# ---------------------------------------------------------------------------
# Task 2: Clean it
# ---------------------------------------------------------------------------
num_cols = ["Quantity", "Price Per Unit", "Total Spent"]

# Numbers stored as text because of 'UNKNOWN'/'ERROR' -> turn junk into NaN
for col in num_cols:
    junk = raw[col].isin(["UNKNOWN", "ERROR"]).sum()
    before = df[col].isna().sum()
    df[col] = pd.to_numeric(df[col], errors="coerce")
    after = df[col].isna().sum()
    print(col, "NaN before:", before, "-> after:", after, "| placeholders in raw:", junk)
    # check: (after - before) should equal junk, otherwise real values were destroyed

# Rule check on complete rows: Total = Quantity x Price
complete = df.dropna(subset=num_cols)
match = np.isclose(complete["Total Spent"], complete["Quantity"] * complete["Price Per Unit"])
print("complete rows:", len(complete), "| matches:", match.sum(), "| mismatches:", (~match).sum())

# Menu: typed by hand, then PROVED against the data so a typo cannot hide
menu = {"Cake": 3.0, "Coffee": 2.0, "Cookie": 1.0, "Salad": 5.0,
        "Sandwich": 4.0, "Smoothie": 4.0, "Juice": 3.0, "Tea": 1.5}
seen = df.groupby("Item")["Price Per Unit"].agg(lambda s: set(s.dropna()))
for item, price in menu.items():
    assert seen[item] == {price}, f"menu mismatch for {item}: data says {seen[item]}"

# 1) Price from menu (works even when Quantity/Total are missing)
before = df["Price Per Unit"].isna().sum()
df["Price Per Unit"] = df["Price Per Unit"].fillna(df["Item"].map(menu))
print("Price filled from menu:", before - df["Price Per Unit"].isna().sum())

# 2) Total = Quantity x Price
mask = df["Total Spent"].isna() & df["Quantity"].notna() & df["Price Per Unit"].notna()
print("rows fixed (Total):", mask.sum())
df.loc[mask, "Total Spent"] = df.loc[mask, "Quantity"] * df.loc[mask, "Price Per Unit"]

# 3) Quantity = Total / Price (then validate)
mask = df["Quantity"].isna() & df["Total Spent"].notna() & df["Price Per Unit"].notna()
print("rows fixed (Quantity):", mask.sum())
df.loc[mask, "Quantity"] = df.loc[mask, "Total Spent"] / df.loc[mask, "Price Per Unit"]
q = df["Quantity"]
bad = q.notna() & ((q % 1 != 0) | (q < 1) | (q > 5))
print("bad Quantity values:", bad.sum())
assert bad.sum() == 0

# 4) Price = Total / Quantity
mask = df["Price Per Unit"].isna() & df["Total Spent"].notna() & df["Quantity"].notna()
print("rows fixed (Price from Total/Quantity):", mask.sum())
df.loc[mask, "Price Per Unit"] = df.loc[mask, "Total Spent"] / df.loc[mask, "Quantity"]

# Rows with 2+ of the 3 corners missing cannot be recovered -> drop
left = df[df[num_cols].isna().any(axis=1)]
print("unrecoverable rows:", len(left), f"({len(left) / len(df):.2%})")
print(left["Item"].value_counts(dropna=False))      # not concentrated in one item?
df = df.dropna(subset=num_cols).copy()
df["Quantity"] = df["Quantity"].round().astype(int)

# Proof that repairs did not corrupt anything
print("mismatches after repair:",
      (~np.isclose(df["Total Spent"], df["Quantity"] * df["Price Per Unit"])).sum())

# Text columns: placeholders -> NaN, recover Item where the price is unique
text_cols = ["Item", "Payment Method", "Location"]
df[text_cols] = df[text_cols].replace(["UNKNOWN", "ERROR"], np.nan)
price_to_item = {1.0: "Cookie", 1.5: "Tea", 2.0: "Coffee", 5.0: "Salad"}   # 3.0 and 4.0 are ambiguous
m = df["Item"].isna() & df["Price Per Unit"].isin(price_to_item)
df.loc[m, "Item"] = df.loc[m, "Price Per Unit"].map(price_to_item)
print("Item recovered from unique price:", m.sum())
print(df[text_cols].isna().sum())
print("Share unknown Payment Method by Item (is it tied to one item?):")
print(df.groupby("Item", dropna=False)["Payment Method"].apply(lambda s: s.isna().mean()).round(2))
df[text_cols] = df[text_cols].fillna("Unknown")

# Dates
df["Transaction Date"] = pd.to_datetime(df["Transaction Date"], errors="coerce")
print("bad dates (NaT):", df["Transaction Date"].isna().sum())

print("Final shape:", df.shape)
df.to_csv(Path(__file__).with_name("cafe_clean.csv"), index=False)

# ---------------------------------------------------------------------------
# CLEANING LOG  (numbers from your own output; fill the ones marked ??? after running)
# - Types: Quantity/Price/Total were text because of 'UNKNOWN'/'ERROR'; to_numeric(errors='coerce').
#   Check: new NaN == placeholders in raw (Total: 329 -> matches).
# - Rule Total = Quantity x Price held on 8,544 of 8,544 complete rows -> safe to use for repairs.
# - Price: each real item has exactly one price (menu asserted against data) -> 479 filled from Item.
# - Total: Quantity x Price -> 479 rows.   Quantity: Total / Price -> 456 rows, 0 bad values.
# - Price from Total / Quantity -> 48 rows.   0 mismatches after repair.
# - Dropped 26 rows (0.26%): two or more of Quantity/Price/Total missing, nothing to recover from.
# - Item: 969 placeholder/NaN; recovered ??? where price is unique (1.0/1.5/2.0/5.0);
#   3.0 (Cake/Juice) and 4.0 (Sandwich/Smoothie) NOT guessed -> label 'Unknown'.
# - Payment Method (3,178) and Location (3,961): kept as 'Unknown' category. Dropping would lose
#   ~60% of rows; filling with the mode would invent ~1/3 of the column.
# - Transaction Date: 460 unusable (4.6%) -> kept as NaT; excluded only from time charts.
# - Duplicates: 0 duplicate rows, 10,000 unique Transaction IDs.
# ---------------------------------------------------------------------------

# Task 3: Look for patterns
# - Outliers: Quantity 1-5, Price 1.0-5.0, Total max 25 = 5 x 5 -> all legitimate, log "no outliers"

# - Chart 1: bar, mean Total Spent by Item     (compares categories)
sns.barplot(data=df, x="Item", y="Total Spent", errorbar=None)
plt.title("Mean Total Spent by Item")
plt.show()

# - Chart 2: histogram of Total Spent          (shows distribution shape)
sns.histplot(data=df, x="Total Spent", bins=20, kde=True)
plt.title("Distribution of Total Spent")
plt.show()

# - Chart 3: line, monthly total sales         (trend over time; drop NaT dates first)
monthly_sales = (
    df.dropna(subset=["Transaction Date"])
      .set_index("Transaction Date")
      .resample("ME")["Total Spent"]
      .sum()
      .reset_index()
      .rename(columns={"Transaction Date": "Month"})
)

sns.lineplot(data=monthly_sales, x="Month", y="Total Spent")
plt.title("Monthly Total Sales")
plt.show()

# - One-line reason under each chart
# Chart 1: Shows the average amount spent on each item category.
# Chart 2: Displays the distribution of total spending across all transactions.
# Chart 3: Illustrates the trend in monthly sales over time.

# Task 4: Feature-signal check (same method as Day 8)
# - Question: "Do Location, Payment Method, or weekday change how much a customer spends?"
# - Target: Total Spent. Compare with groupby + mean + count.
# - Item, Quantity, Price Per Unit: mark DUPLICATE / formula (Total = Quantity x Price), not signal.
# - Mark each feature: keep / drop / duplicate / leakage risk

df["Weekday"] = df["Transaction Date"].dt.day_name()

for feature in ["Location", "Payment Method", "Weekday"]:
    print(f"\n### Feature signal: {feature}")
    summary = (
        df.groupby(feature, dropna=False)["Total Spent"]
          .agg(["mean", "count"])
          .reset_index()
          .rename(columns={"mean": "avg_total_spent", "count": "transactions"})
          .sort_values("avg_total_spent", ascending=False)
    )
    print(summary.head(10))
    print("Range in avg spend:", summary["avg_total_spent"].max() - summary["avg_total_spent"].min())
    print("Distinct groups:", summary[feature].nunique())

# Feature decisions should be based on whether a feature meaningfully changes average spend.
# In this dataset, Item, Quantity, and Price Per Unit are duplicate or formula-derived fields,
# not useful business signal. Location and Payment Method are the first features worth checking
# as likely spend drivers. Weekday is valid if it changes spend enough to matter. If a feature
# directly leaks target information or reconstructs the target, mark it as leakage risk instead.

# Example final labels:
# - Item: duplicate
# - Quantity: duplicate / formula-derived
# - Price Per Unit: duplicate / formula-derived
# - Location: keep if average spend changes materially; otherwise drop
# - Payment Method: keep if average spend changes materially; otherwise drop
# - Weekday: keep if average spend changes materially; otherwise drop
