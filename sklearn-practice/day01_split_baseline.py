# Dataset: from sklearn.datasets import load_wine   (use as_frame=True)

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
data = load_wine(as_frame=True)

# Task 1:
# - Load the wine dataset into X and y
# - Print X.shape and the class counts of y (value_counts, sorted by class)
# - Predict BEFORE running: which class is the majority, and what accuracy will "always predict majority" get on the full data? (write your prediction as a comment)
# Prediction: class 1 is the majority. If we always predict the majority class, the accuracy on the full dataset should be around 40% because about 71 out of 178 samples belong to class 1.

X, y = data.data, data.target
print(X.shape)
print(y.value_counts().sort_index().to_dict())

# Task 2:
# - Split with test_size=0.25, random_state=7, stratify=y
# - Print len(X_train), len(X_test)
# - Predict BEFORE running: how many rows in each?
# - Print class counts of y_train and y_test. Why are they not exactly 75/25 per class? (answer in a comment)
# Prediction: 25% of 178 is 44.5, so the test split should have 45 rows and the train split 133.
# The full-data class counts are 59, 71, and 48. A quarter of each is 14.75, 17.75, and 12;
# rows cannot be split, and the counts must total 45, so stratification keeps them close rather than exact.

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=7, stratify=y)
print(len(X_train))
print(len(X_test))
print(y_train.value_counts().sort_index().to_dict())
print(y_test.value_counts().sort_index().to_dict())

# Task 3:
# - Fit DummyClassifier(strategy="most_frequent") on the TRAIN data
# - Print its test accuracy
# - Print set(baseline.predict(X_test))
# - Predict BEFORE running: how many different values will that set contain, and why?
# Prediction: the set will contain exactly one value because most_frequent predicts the training majority class for every sample.

baseline = DummyClassifier(strategy="most_frequent")
baseline.fit(X_train, y_train)
print(baseline.score(X_test, y_test))
print(set(baseline.predict(X_test)))

# Task 4:
# - Fit LogisticRegression(max_iter=5000) on the train data
# - Print train accuracy AND test accuracy
# - In a comment: does it beat the baseline? By how many points?
# - In a comment: which is higher, train or test, and what does a big gap between them mean?
# LogisticRegression test accuracy is 93.3% versus the 40.0% baseline, a gain of 53.3 percentage points.
# Train accuracy is 100.0%, 6.7 points above test accuracy; a large gap can indicate overfitting.

# Wine features have very different scales, so LogisticRegression may emit a ConvergenceWarning; scaling is covered on Day 12.
model = LogisticRegression(max_iter=5000)
model.fit(X_train, y_train)
print(model.score(X_train, y_train))
print(model.score(X_test, y_test))

# Task 5 (the trap):
# - Run the split twice with random_state=7 and compare X_test.index. Same or different?
# - Run it twice with NO random_state. Same or different?
# - Comment: why does this matter when you report results to a client?
# Explanation: with the same random_state, the split is reproducible and the same rows appear in the test set each time.
# Without random_state, sklearn/NumPy's random number generator produces a different split on each run.
# Unreproducible results are hard to audit, and rerunning until a score looks flattering is test-set cheating.

same_split_first = train_test_split(X, y, test_size=0.25, random_state=7, stratify=y)
same_split_second = train_test_split(X, y, test_size=0.25, random_state=7, stratify=y)
print(same_split_first[1].index.equals(same_split_second[1].index))

unseeded_split_first = train_test_split(X, y, test_size=0.25, stratify=y)
unseeded_split_second = train_test_split(X, y, test_size=0.25, stratify=y)
print(unseeded_split_first[1].index.equals(unseeded_split_second[1].index))