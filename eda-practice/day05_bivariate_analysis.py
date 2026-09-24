import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
df = sns.load_dataset("titanic")

# Task 1: Number vs number — age and fare
# - PREDICT FIRST: do you expect age and fare to be strongly correlated,
#   weakly correlated, or basically unrelated? Why? (think about whether
#   older passengers logically would have paid more)
# - Compute df[['age','fare']].corr()
# - Make a scatterplot: sns.scatterplot(x='age', y='fare', data=df)

# I dint think so age and fare are related they are absically unrelated. Any age of people can buy 1st class tickets and same for other classes.
print("Relation between age & fare")
print(df[['age','fare']].corr())

sns.scatterplot(x='age', y='fare', data=df)
plt.show()

# Task 2: Category vs number — pclass and fare
# - PREDICT FIRST: which class do you expect to have the highest average fare
# - Compute df.groupby('pclass')['fare'].mean()
# - Make a boxplot: sns.boxplot(x='pclass', y='fare', data=df)

# 1st class will have highest average because they have most expensive tickets.
print("Average fare per class")
print(df.groupby('pclass')['fare'].mean())

sns.boxplot(x='pclass', y='fare', data=df)
plt.show()

# Task 3: Category vs category — pclass and survived
# - PREDICT FIRST: which class do you expect had the highest survival rate
# - Compute a crosstab: pd.crosstab(df['pclass'], df['survived'], normalize='index')
# - This gives you survival RATE per class, not raw counts — explain in a
#   comment why normalize='index' matters here vs. just raw counts

# 1st class will have highest survival becuase they have closed cabins and they are close to the lifeboats.
print("Highest survival rate per class")
print(pd.crosstab(df['pclass'], df['survived'], normalize='index'))
# with normalize index you get percentage within each rows instead of raw numbers.

# Task 4: Category vs category — sex and survived
# - Same as Task 3, but for sex instead of pclass
# - This one has a strong, well-known historical pattern — predict it first

# Women will likely have a higher survival rate than men because women and
# children were generally given priority when lifeboats were loaded.
print("Highest survival rate base on gender")
print(pd.crosstab(df['sex'], df['survived'], normalize='index'))

# Task 5: The causation trap
# - Write 2-3 sentences: pclass correlates with survival, but what's the
#   actual likely REASON (the hidden third factor), not just "1st class =
#   better luck"

# Pclass did not cause survival; physical proximity to the lifeboats did.
# Pclass was a strong stand-in for that proximity because first-class cabins
# were located on the upper decks.
# Fare-by-class: 1st class averages ~4x 2nd class fare and ~6x 3rd class fare — confirms prediction.
# Sex/survival: females survived at 74.2% vs males at 18.9%, a 55-point gap — strongest pattern in the dataset.