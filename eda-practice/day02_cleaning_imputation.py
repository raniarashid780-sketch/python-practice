import pandas as pd
import seaborn as sns
# Task 1: Classify the missingness mechanism
# - For `age`: before imputing anything, investigate whether age is missing
#   randomly or systematically. Check: does missingness in age correlate with
#   pclass or sex? (hint: group by pclass, count how many age values are null
#   in each group, compare rates)
# - PREDICT FIRST: do you expect age to be missing more in 1st class or 3rd
#   class, and why, before you run the check
# - State your conclusion: is age's missingness closer to MCAR or MAR?

df = sns.load_dataset("titanic")
# I think 3rd class has more missing age
print(df[df["age"].isnull()]["pclass"].value_counts())
# so it is MAR case maybe the person who was writing the numbers was tired or less careful in 3rd class

# Task 2: Impute `age` properly
# - Do NOT use a single global median for the whole column
# - Instead, compute median age grouped by pclass and sex (a 2-way group),
#   and fill each missing age with its group's median
# - Verify: after imputing, confirm df['age'].isnull().sum() == 0

print(df.groupby(["pclass", "sex"])["age"].median())
group_medians = df.groupby(["pclass", "sex"])["age"].transform("median")

df["age"] = df["age"].fillna(group_medians)

print(df["age"].isnull().sum())

# Task 3: Impute `embarked`
# - Only 2 missing values, and embarked is categorical — use mode imputation
#   (df['embarked'].mode()[0])
# - Justify in a comment: why mode instead of median/mean makes sense here
#   (think about what "average port" would even mean)

most_common_port = df["embarked"].mode()[0]
df["embarked"] = df["embarked"].fillna(most_common_port)

print(df["embarked"].isnull().sum())
# I am using mode here not mean or median beause it is not numbers it is port you cant take average of port instead you can take most common port as everyone else.


# Task 4: Finalize deck's fate
# - You called this in Day 1 (drop). Now actually do it: df.drop(columns=['deck'])
# - In a comment, name the one scenario where you'd keep a 77%-missing column
#   instead of dropping it (hint: think about what a missing deck value might
#   itself be telling you, independent of what deck they were on)

df = df.drop(columns=['deck'])
# Keep deck if missingness itself carries useful information,
# such as indicating that no deck was assigned or recorded.
df = df.drop(columns=['alive', 'class', 'adult_male', 'embark_town'])
# dropping all the duplicate columns too

# Task 5: Verify the whole cleaning pass
# - Run df.isnull().sum() one more time — every column should now read 0
#   except any you deliberately dropped
# - Write a short "cleaning log" comment: what you did to each problem column
#   and why, in 4-5 lines total

print(df.isnull().sum())
# Cleaning log:
# Filled missing ages using the median for each passenger class and sex.
# Filled missing embarked values with the most common port.
# Dropped deck because most of its values were missing.
# Dropped duplicate or repeated information columns.