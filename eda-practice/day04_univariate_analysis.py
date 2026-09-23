import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset("titanic")

# Task 1: Distribution shape of `fare`
# - PREDICT FIRST: will mean or median be higher for fare, and why (think
#   about yesterday's 116 high outliers)
# - Compute df['fare'].mean() and df['fare'].median(), compare to your guess
# - Plot a histogram: sns.histplot(df['fare'])

# mean will be higher because their are high outliers in data that keeps the mean high
# median will be low or in mid because it is the centre of the column
print(f"Mean of fare column :{df['fare'].mean()}")
print(f"Median of fare column :{df['fare'].median()}")

sns.histplot(df['fare'])
plt.show()

# Task 2: Distribution shape of `age`
# - Same as above: predict mean vs median for age first, then check
# - Age should look more "normal" (bell-shaped) than fare — plot it and see
#   if that holds

# for age column mean and median will be almost same because there were no such and low outliers in the data
print(f"Mean of age column :{df['age'].mean()}")
print(f"Median of age column :{df['age'].median()}")

sns.histplot(df['age'])
plt.show()

# Task 3: Skewness, with a number not just a picture
# - Compute df['fare'].skew() and df['age'].skew()
# - A skew near 0 = symmetric, positive = long right tail, negative = long
#   left tail. Match the numbers to what your histograms showed

print(f"Fare:{df['fare'].skew()}")
print(f"Age:{df['age'].skew()}")

# Task 4: Categorical variables — counts, not shape
# - For `pclass`, `sex`, `embarked`: print value_counts() and value_counts(normalize=True)
# - Which class/sex/port dominates the dataset? Is that expected given what
#   you know about the Titanic historically?

print(f"Pclass:{df['pclass'].value_counts()}")
print(f"Pclass: {df['pclass'].value_counts(normalize=True)}")
print(f"Sex:{df['sex'].value_counts()}")
print(f"Sex:{df['sex'].value_counts(normalize=True)}")
print(f"Embarked:{df['embarked'].value_counts()}")
print(f"Embarked:{df['embarked'].value_counts(normalize=True)}")

print("The 3rd class dominates the dataset with 3rd class = 491, 2nd class = 216 and 1st class = 184 it was expected from previous analysis.")
print("The sex that dominates the dataset is male with male = 577 and female = 314")
print("The most dominated port is S")

# Task 5: One-line takeaway per variable
# - Write a short comment for fare, age, pclass: what's the shape, and what
#   would that mean for choosing mean vs median if you needed one number to
#   summarize each

# Fare is strongly right-skewed, so the median is a better typical value than the mean.
# Age is mildly right-skewed, so the median is slightly more robust, although mean and median are fairly close.
# Pclass is categorical/ordinal, so use the mode or class proportions instead of the mean or median.
