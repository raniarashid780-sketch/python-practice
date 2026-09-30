import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = sns.load_dataset("titanic")

# Task 1: Match chart to variable type, no code yet
# - For each of these, name the correct chart type BEFORE writing any code:
#   (a) distribution of `age`   -> Histogram
#   (b) count of passengers per `pclass` -> Count plot / bar chart
#   (c) `fare` vs `age` -> Scatterplot
#   (d) survival rate by `sex` -> Bar chart (with survival mean)
#   (e) survival rate by `pclass` AND `sex` together -> Grouped bar chart

# Task 2: Build (a) through (d)
# (a) Distribution of age
sns.histplot(df['age'], bins=20, kde=True)
plt.title('Age Distribution')
plt.show()

# (b) Count of passengers per class
sns.countplot(x='pclass', data=df)
plt.title('Passengers by Class')
plt.show()

# (c) Fare vs age
sns.scatterplot(x='age', y='fare', data=df)
plt.title('Fare vs Age')
plt.show()

# (d) Survival rate by sex
sns.barplot(x='sex', y='survived', data=df, estimator='mean')
plt.title('Survival Rate by Sex')
plt.ylabel('Survival rate')
plt.show()

# Task 3: Handle (e) — two categories at once
sns.catplot(x='pclass', y='survived', hue='sex', kind='bar', data=df, estimator='mean')
plt.title('Survival Rate by Class and Sex')
plt.show()
# The sex gap remains inside each class: women still survive much more often
# than men in every class, even though the gap is not exactly the same in all classes.

# Task 4: The pie chart test
# Pie chart of pclass counts
pclass_counts = df['pclass'].value_counts()
pclass_counts.plot.pie(autopct='%1.1f%%')
plt.title('Passenger Distribution by Class (Pie Chart)')
plt.show()

# Now compare with the bar chart from Task 2
# The bar chart is easier to read because the eye can compare bar heights more
# directly. It is clearer that 1st class has more passengers than 2nd class,
# while pie slices are harder to compare visually when several categories are shown.

# Extra check: print raw counts to compare classes directly
print(df['pclass'].value_counts())