# Dataset: from sklearn.datasets import load_wine   (use as_frame=True)

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
data =load_wine(as_frame=True)

# Task 1:
# - Load the wine dataset into X and y
# - Print X.shape and the class counts of y (value_counts, sorted by class)
# - Predict BEFORE running: which class is the majority, and what accuracy will "always predict majority" get on the full data? (write your prediction as a comment)
# Prediction: class 1 is the majority. If we always predict the majority class, the accuracy on the full dataset should be around 40% because about 71 out of 178 samples belong to class 1.

X, y = data.data, data.target
print(X.shape)
print(y.value_counts().to_dict())

# Task 2:
# - Split with test_size=0.25, random_state=7, stratify=yexpal
# - Print len(X_train), len(X_test)
# - Predict BEFORE running: how many rows in each?
# - Print class counts of y_train and y_test. Why are they not exactly 75/25 per class? (answer in a comment)
# Prediction: with 20% test size and 178 total rows, we expect about 142 rows in train and 36 in test.
# The class counts will not be exactly 80/20 for each class because the dataset is not perfectly divisible by 5, and stratify keeps the proportions close but not exact.

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
print(len(X_train))
print(X_test.shape)

# Task 3:
# - Fit DummyClassifier(strategy="most_frequent") on the TRAIN data
# - Print its test accuracy
# - Print set(baseline.predict(X_test))
# - Predict BEFORE running: how many different values will that set contain, and why?
# Prediction: the set will usually contain only one value, because the dummy baseline predicts the same majority class for every sample.

baseline = DummyClassifier(strategy="most_frequent")
baseline.fit(X_train, y_train)
print(baseline.score(X_test, y_test))
print(set(baseline.predict(X_test)))

# Task 4:
# - Fit LogisticRegression(max_iter=5000) on the train data
# - Print train accuracy AND test accuracy
# - In a comment: does it beat the baseline? By how many points?
# - In a comment: which is higher, train or test, and what does a big gap between them mean?
# Prediction: the logistic regression model should beat the baseline by a large margin, roughly 50+ percentage points.
# Training accuracy is usually higher than test accuracy. A big gap suggests overfitting: the model fits the training data very well but does not generalize as well to new data.

model = LogisticRegression(max_iter=5000)
model.fit(X_train, y_train)
print(model.score(X_train, y_train))
print(model.score(X_test, y_test))

# Task 5 (the trap):
# - Run the split twice with random_state=7 and compare X_test.index. Same or different?
# - Run it twice with NO random_state. Same or different?
# - Comment: why does this matter when you report results to a client?
# Explanation: with the same random_state, the split is reproducible and the same rows appear in the test set each time.
# Without random_state, Python chooses a different random split every run, so your reported accuracy may change from one run to the next.
# This matters in real reporting because results should be consistent and reproducible for fair comparisons and client communication.

same_split = train_test_split(X, y, test_size=0.2, random_state=7, stratify=y)
print(same_split[1].index.equals(X_test.index))  # Should be True