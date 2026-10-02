import seaborn as sns

df = sns.load_dataset("titanic")

# Task 1: Audit the columns that are actually in this dataset.
print("Dataset columns:")
print(df.columns.tolist())

# These columns describe passengers before the outcome and can be candidate inputs.
known_before_outcome = [
	'pclass', 'sex', 'age', 'sibsp', 'parch', 'fare', 'embarked',
	'who', 'adult_male', 'alone', 'class', 'deck', 'embark_town'
]
print("\nKnown-before-outcome columns:")
print([column for column in known_before_outcome if column in df.columns])

# survived is the target; alive duplicates it exactly. class duplicates pclass.
# who/adult_male and alone are redundant derived features, not outcome leakage.
print("\nLeakage and duplicate checks:")
print("alive exactly matches survived:", df['alive'].eq(df['survived'].map({0: 'no', 1: 'yes'})).all())
print("class matches pclass:", df['class'].eq(df['pclass'].map({1: 'First', 2: 'Second', 3: 'Third'})).all())
print("Columns absent from this dataset:", [column for column in ['boat', 'body', 'home.dest', 'ticket', 'name'] if column not in df.columns])

# Task 2: Check embarked within both pclass and sex. Counts expose small groups.
print("\nSurvival by pclass and embarked:")
print(df.groupby(['pclass', 'embarked'])['survived'].agg(['mean', 'count']).round(3))

print("\nSurvival by pclass, sex, and embarked:")
print(df.groupby(['pclass', 'sex', 'embarked'])['survived'].agg(['mean', 'count']).round(3))

# Compare rates only within the same class and sex; use counts to judge reliability.
# A port difference that persists in these groups may carry signal beyond pclass/sex.

# Task 3: Check whether deck missingness itself is associated with survival.
df['deck_missing'] = df['deck'].isna()
print("\nSurvival by whether deck is missing:")
print(df.groupby('deck_missing')['survived'].agg(['mean', 'count']).round(3))
# Deck is recorded for only a minority of passengers; its missingness is associated
# with survival, so treating missing deck as an ordinary weak feature can leak signal.

# Task 4: Test family features before deciding whether to keep them.
print("\nSurvival by number of siblings/spouses aboard:")
print(df.groupby('sibsp')['survived'].agg(['mean', 'count']).round(3))
print("\nSurvival by number of parents/children aboard:")
print(df.groupby('parch')['survived'].agg(['mean', 'count']).round(3))

# Keep sibsp and parch as candidate features: rates vary across group sizes, but
# the small counts at larger values mean those estimates need caution. Drop alone
# because it is derived from family information already represented by these columns.

# Final beginner feature set, decided after checking family survival rates.
features = ['sex', 'pclass', 'age', 'fare', 'embarked', 'alone', 'family_size_binned']
# excluded: survived (target), alive (duplicate), class/embark_town (duplicates),
# who/adult_male (derived from sex+age), deck (missingness tied to outcome),
# sibsp/parch (replaced by family size)
print("\nFinal candidate features:")
print(features)

# Exclude survived (target), alive (target duplicate), and class (pclass duplicate).
# who, adult_male, and alone are redundant derived columns. Exclude deck because
# its missingness is outcome-associated; embark_town duplicates embarked.

# 1. family size
df['family_size'] = df['sibsp'] + df['parch'] + 1
print(df.groupby('family_size')['survived'].agg(['mean', 'count']))
print(df.groupby('alone')['survived'].agg(['mean', 'count']))

# 2. alone vs embarked
print(df.groupby(['alone', 'embarked'])['survived'].agg(['mean', 'count']))

# 3. deck missing, inside each class
print(df.groupby(['pclass', 'deck_missing'])['survived'].agg(['mean', 'count']))

# 4. age and fare: median for survivors vs non-survivors
print(df.groupby('survived')[['age', 'fare']].median())