import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Task 1: Find outliers in `fare` using IQR
# - PREDICT FIRST: which direction do you expect outliers in fare to be —
#   suspiciously high, suspiciously low, or both? Why? (think about what you
#   already know: fare=0.0 exists and you explained it in Day 1)
# - Compute Q1, Q3, IQR, lower_fence, upper_fence for `fare`
# - Print how many rows fall below lower_fence and how many fall above upper_fence

df = sns.load_dataset("titanic")
Q1 = df['fare'].quantile(0.25)   # the value 25% of the way up
Q3 = df['fare'].quantile(0.75)   # the value 75% of the way up
IQR = Q3 - Q1
lower_fence = Q1 - 1.5 * IQR
upper_fence = Q3 + 1.5 * IQR

print("Fares below the lower fence:", (df["fare"] < lower_fence).sum())
print("Fares above the upper fence:", (df["fare"] > upper_fence).sum())

# Task 2: Look at the actual outlier rows, don't just count them
# - Filter df to show the rows where fare is above upper_fence
# - Look at their pclass — is there a pattern? (hint: which class would have
#   the most expensive tickets, obviously — but does the data actually confirm it?)

fare_outliers = df[df["fare"] > upper_fence]
print("Rows with fares above the upper fence:")
print(fare_outliers[["pclass", "fare", "embarked"]])
print("High-fare tickets by passenger class:")
print(fare_outliers["pclass"].value_counts().sort_index())

# Task 3: Z-score check on `age`
# - Compute z-scores for `age` (use the imputed age column from Day 2)
# - Print how many rows have |z-score| > 3
# - Are these the same rows IQR would have flagged, or different ones?
#   (they don't always agree — that's expected, and worth noticing)

# Use the same grouped-median approach from Day 2 before checking age.
age_group_medians = df.groupby(["pclass", "sex"])["age"].transform("median")
df["age"] = df["age"].fillna(age_group_medians)

age_z_scores = stats.zscore(df["age"])
print("Age rows with an absolute z-score above 3:",
	(np.abs(age_z_scores) > 3).sum())

age_q1 = df["age"].quantile(0.25)
age_q3 = df["age"].quantile(0.75)
age_iqr = age_q3 - age_q1
age_upper_fence = age_q3 + 1.5 * age_iqr
age_iqr_outliers = df[df["age"] > age_upper_fence]
print("Age rows above the IQR upper fence:", len(age_iqr_outliers))

# Task 4: Make the real decision
# - For the fare outliers: are these mistakes to remove, or real expensive
#   tickets to keep? State your verdict with a reason, not just "keep" or "drop"
# - For any age outliers: same question — investigate before deciding anything

print("Decision: keep the fare outliers. They are mostly expensive tickets, "
	"not automatically incorrect data.")
print("Decision: investigate age outliers before removing them. A very young "
	"or old passenger can be a real passenger, not a data error.")

# Task 5: Visualize it
# - Make one boxplot for `fare` using seaborn (sns.boxplot(x=df['fare']))
# - Write one line: does the boxplot visually agree with what your IQR numbers said?


sns.boxplot(x=df['fare'])
plt.title("Titanic fares and possible outliers")
print("The boxplot agrees with the IQR calculation: it shows several "
	"unusually high fares on the right side.")
plt.show()