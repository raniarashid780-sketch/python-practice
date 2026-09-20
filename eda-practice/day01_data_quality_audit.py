import seaborn as sns
import pandas as pd

# Task 1: Structural check
# - Load the titanic dataset via sns.load_dataset('titanic')
# - PREDICT FIRST, before running anything: how many rows and columns do you
#   expect, and name 3 columns you'd guess have missing values, ranked by
#   how much you think is missing (most to least). Write this as a comment.
# - Then run df.shape, df.dtypes, df.info() and compare to your prediction

# Prediction before running the data check:
# According to my knowledge titanic has about 2250 passengers so it will have about 2250 columns and about 10-15 columns eg: survived, died, age, fare, gender etc
df = sns.load_dataset('titanic')
print("shape of data set")
print(df.shape)
print("data types per column")
print(df.dtypes)
print("total info")
print(df.info())
# The data set has 891 rows and 15 columns so the data set is 40% of actual population so its a sample dataset.

# Task 2: Missing value audit
# - Compute isnull().sum() AND isnull().mean()*100 — print both, don't just eyeball counts
# - Identify: which columns have >50% missing? >90%? These are candidates for
#   dropping entirely, not imputing — a column that's 90%+ empty carries almost
#   no signal and imputing it mostly means "making up data"
# - Write a one-line verdict per flagged column: keep / drop / investigate further

print("sum of null values per column")
print(df.isnull().sum())
print("percentage of null values per column")
print(df.isnull().mean()*100)
# The column deck has about 77% missing values so we should drop it because keeping it will mean making fake data
# age: 19% missing — verdict: keep becuase its almost complete
# embarked: 0.25% missing — verdict: keep becuase its almost complete

# Task 3: Duplicate check
# - Run df.duplicated().sum() for full-row duplicates
# - This dataset has no natural unique ID column — explain in a comment why
#   that makes full-row duplicate checking weaker evidence here than it would
#   be on a dataset with a real ID column

print("duplicate values")
print(df.duplicated().sum())
# Without a unique passenger ID, a matching row could be the same person
# duplicated, or two different passengers who coincidentally share every
# recorded trait (age, class, fare, etc.). So 107 is weak evidence of real
# duplication, not proof of it.

# Task 4: Type audit
# - For every column, check: does the pandas dtype (df.dtypes) actually match
#   what the column semantically IS? (e.g. is 'pclass' really numeric, or is
#   it actually a category wearing an int64 costume?)
# - Run df.nunique() and flag: any column with only 2-4 unique values that's
#   stored as int/float/object should be flagged as "should be categorical"
# - List every column you're reclassifying and why

print("Unique values")
print(df.nunique())

# Task 5: Validity / range check (the placeholder-hunting step)
# - For every NUMERIC column: print min and max. Flag anything impossible
#   (e.g. negative age, fare of exactly 0 for a paid passenger, age of 0.42 —
#   is that a data entry error or something else? investigate before deciding)
# - For every OBJECT/categorical column: print .unique() and scan for
#   suspicious values that aren't NaN but are functionally "missing"
#   (empty strings, '?', inconsistent capitalization like 'Male' vs 'male')

print("survived column")
print(df["survived"].min())
print(df["survived"].max())
print("pclass column")
print(df["pclass"].min())
print(df["pclass"].max())
print("age column")
print(df["age"].min())
print(df["age"].max())
print("sibsp column")
print(df["sibsp"].min())
print(df["sibsp"].max())
print("fare column")
print(df["fare"].min())
print(df["fare"].max())
print("parch column")
print(df["parch"].min())
print(df["parch"].max())
print("sex column")
print(df["sex"].unique())
print("deck column")
print(df["deck"].unique())
print("embark_town column")
print(df["embark_town"].unique())
print("alive column")
print(df["alive"].unique())
print("alone column")
print(df["alone"].unique())
print("embarked column")
print(df["embarked"].unique())
print("who column")
print(df["who"].unique())
print("class column")
print(df["class"].unique())
print("adult_male column")
print(df["adult_male"].unique())
print("difference b/w who and adult_male")
print(df.groupby(['who', 'adult_male']).size())


# Task 6: Write the audit report
# - As a docstring or comment block at the bottom of the file, write an actual
#   short report: dataset shape, list of quality issues found (missingness,
#   duplicates, type mismatches, validity problems), and a keep/drop/fix
#   recommendation per problem column
# - This report is the actual deliverable of Day 1 — the code is just how you
#   got there

report = """
Titanic data audit report
========================

Dataset shape: 891 rows x 15 columns

Main issues found:
- The biggest missing-value problem is `age`, followed by `deck` and then `embarked`.
- `deck` is very incomplete, so it is probably not useful without a lot of cleanup.
- There are no obvious full-row duplicates, but duplicate checking is weak because there is no proper unique ID.
- Some columns are conceptually categorical but stored in a less friendly dtype.
- Numeric ranges mostly look reasonable, but they still need a sanity check before analysis.

Recommendation:
- `age`: keep, but investigate missing values and maybe impute later.
- `embarked`: keep and fix missing values if needed.
- There is one catch in age column the min value is 0.42 which is (0.42 * 12) 5.04 months that is a point worth noticing.
- `fare`: min fare is 0.0 that is an edge case it can be someone who dint pay.
- `deck`: likely drop or treat as low-value because it is too incomplete.
- `who/adult_male`: are somehow common but not exact duplicate who tells the person is woman, man, or child and adult_male just tells is it adultmale or not.
- `pclass`, `survived`, `sex`, and similar columns: convert to category when useful for analysis.

Overall: the dataset is good for learning and basic EDA, but it still needs a bit of cleaning before deeper analysis or modeling.
"""

print("\n=== Task 6: Audit report ===")
print(report)

# This is a good reminder that real-world data is almost never perfectly clean.
# The job is not to avoid messy data completely, but to understand it and handle it carefully.
