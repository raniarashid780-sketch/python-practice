# Task 1: State the modeling goal explicitly
# - Write one sentence: "The goal is to predict [target] using [what kind of
#   inputs]." For Titanic, the natural target is `survived`.
# - Name the target column and whether it's binary, multi-class, or continuous

# The goal is to predict who survived using sex, pclass, fare, age, and embarked as inputs.
# The target column is survived, and it is binary because it has only two values: 0 and 1.

# Task 2: Revisit every finding from Days 1-5 through THIS lens
# - Go back through your five files. For each major finding (missingness,
#   outliers, distributions, relationships), write one line: "relevant to
#   predicting survival" or "not directly relevant" — and why
# - Example: fare's right-skew (Day 4) — relevant? age/fare's near-zero
#   correlation (Day 5) — relevant?

# Fare's right-skew matters when preparing the data because a few expensive tickets can affect scaling, but skew alone doesn't show that fare predicts survival.
# Day 1: There were 869 missing cells overall (about 6.5% of all cells); deck alone had 688 missing values (about 77%). This is relevant to preparing the data because missing inputs need to be handled before prediction.
# Day 1: The dataset had 107 duplicate rows. This is not directly conclusive because without a unique passenger ID, identical rows could belong to different people.
# Day 2: I handled missing `age` values by filling with the median grouped by pclass and sex. This matters for prediction because it preserves useful group differences while avoiding missing model inputs.
# Day 2: I handled missing `embarked` values by filling with the most common port (the mode). This matters for prediction because the feature can be retained without inventing an average port.
# Day 3: The fare outlier check found 116 values above the upper fence and none below the lower fence. This is relevant to data preparation, but the high fares are mostly plausible first-class tickets rather than errors to remove.
# Day 3: The age IQR outlier check found 33 values, mostly ages 58-80. This is not directly a data-quality problem because these are plausible passengers, so they should not be removed just for being unusual.
# Day 4: Fare is strongly right-skewed, so this is relevant to preparation because extreme fares can influence some models and transformations, though skew alone does not establish predictive value.
# Day 4: Age is roughly bell-shaped with mild right skew, so this is relevant to preparation because its shape affects how it may be summarized or transformed, not whether it predicts survival.
# Day 4: The dataset has more third-class passengers (491) than first-class passengers (216). This is relevant because class imbalance affects how representative overall summaries are, though it does not itself prove a survival relationship.
# Day 5: Age and fare have a weak positive correlation (about 0.10). This does not show whether either feature predicts survival because it measures the relationship between age and fare, not either feature's relationship with the target.
# Day 5: Survival differs by passenger class by about 39 percentage points (first class about 63%, third class about 24%). This is relevant because it is a substantial observed association with the target.
# Day 5: Survival differs by sex by about 55 percentage points (female about 74%, male about 19%). This is relevant because it is the strongest measured association with the target in these findings.
# Day 5: First-class average fare is about 4 times second-class fare and 6 times third-class fare. This does not directly show that fare predicts survival because fare is associated with pclass, so the relationship could reflect class rather than an independent fare effect.

# Task 3: Rank candidate features by likely usefulness
# - Based on Days 3-5's findings, list pclass, sex, age, fare, embarked in
#   order of how strongly you think each predicts survival
# - Justify the ranking using YOUR OWN numbers from Day 5 (the 55-point sex
#   gap, the 38-point pclass gap) — not a guess, the actual evidence you
#   already collected

# My ranking, from most to least useful, is: 1. sex, 2. pclass, 3. fare,
# 4. age, 5. embarked. I put sex first because the observed survival gap is
# about 55 percentage points. I put pclass second because its observed
# survival gap is about 39 percentage points. The evidence for the remaining
# features is indirect or limited because fare differs by class, age-fare
# correlation is weak and does not measure survival, and no survival result
# for embarked was recorded here.

# Task 4: Spot the leakage risk
# - `alive` was dropped in Day 2 as a redundant duplicate of `survived`.
#   Explain in one sentence why using `alive` as a model INPUT (not target)
#   would be a serious mistake, not just redundant information

# Using `alive` as an input would leak the target because it is an exact
# duplicate of `survived`, which would give misleadingly strong evaluation
# results and would not be available as an independent input for new passengers.