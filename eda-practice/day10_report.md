# Cafe Sales EDA Report

## Question
Do Location, Payment Method, or weekday change how much a customer spends?

## Prediction (written after seeing the output)
I expected the messiest columns to be Payment Method, Location, Transaction Date, and the number columns stored as text.
Result: the number columns were polluted by 'UNKNOWN' and 'ERROR' placeholders, and Location and Payment Method had the most unusable values. My guess was right on which columns, but I did not expect the placeholders to hide inside number columns, because `isnull()` does not count them.

## What the data looked like
- Raw rows: 10,000. Final usable rows: 9,974 (26 dropped, 0.26%)
- Unusable values after cleaning: Payment Method 3,168 and Location 3,952 (counted after the 26 rows were dropped)
- Unusable Transaction Date values: [FILL: the number your script prints for "bad dates (NaT)"]
- The rule Total = Quantity x Price held on 8,544 of 8,544 complete rows, so it was safe to use for repairs
- No duplicate rows, and every Transaction ID is unique

## Cleaning log
- Types: Quantity, Price Per Unit, and Total Spent loaded as text because of 'UNKNOWN' and 'ERROR'. Fixed with `pd.to_numeric(errors="coerce")`
- Price: each real item has exactly one price, so 479 missing prices were filled from the item menu
- Total: 479 rows repaired with Quantity x Price
- Quantity: 456 rows repaired with Total / Price (0 bad values after repair)
- Price: 48 rows repaired with Total / Quantity
- Dropped 26 rows (0.26%): two or more of Quantity, Price, Total were missing, so nothing could be recovered
- Item: 969 placeholder or missing values in the raw data. 489 recovered where the price identifies the item (1.0, 1.5, 2.0, 5.0). The prices 3.0 (Cake/Juice) and 4.0 (Sandwich/Smoothie) are ambiguous, so they were not guessed
- Payment Method and Location: kept as an "Unknown" label. Dropping those rows would lose about 60% of the data, and filling with the most common value would invent about a third of the column
- Transaction Date: unusable dates kept as missing and left out of the time chart only
- Outliers: Quantity 1-5, Price 1.0-5.0, Total max 25 (= 5 x 5). Every value is legitimate, so nothing was removed

## Feature labels
- Item: formula-linked. Item decides Price, and Price x Quantity = Total, so any Item-vs-spend pattern is mechanical, not a discovery
- Quantity, Price Per Unit: formula. Using them to predict Total Spent would be leakage
- Location: drop (gap 0.22, about 2.5% of average spend)
- Payment Method: drop (gap 0.28, about 3.1%)
- Weekday: drop (gap 0.48, about 5.4%)
- The Unknown group was left out of the spend comparison because it is missing data, not a real category

## Charts
1. Bar chart, mean Total Spent by Item. Why a bar: I am comparing categories. What it showed: [FILL: one line. Check whether the tallest bars are just the highest-priced items]
2. Histogram of Total Spent. Why a histogram: I want the shape of one number. What it showed: [FILL: one line]
3. Line chart, monthly total sales. Why a line: time has an order and I want the trend. What it showed: [FILL: one line]

## What I found
Average spend is about 8.93 and the standard deviation is about 6.00.

| Feature | Groups | Typical group size | Gap in average spend | Gap as % of average |
|---|---|---|---|---|
| Location | 2 | [FILL] | 0.2247 | 2.5% |
| Payment Method | 3 | [FILL] | 0.2801 | 3.1% |
| Weekday | 7 | [FILL] | 0.4814 | 5.4% |

How to judge these: even with no real effect, group averages wobble by about 6 divided by the square root of the group size. For about 1,400 transactions per group that is roughly 0.16, so seven weekday averages spread out by about 0.4 from luck alone. The weekday gap of 0.48 is about what chance produces. The Location and Payment Method gaps are small in the same way.

The three gaps cannot be ranked against each other. A range across 7 groups is naturally wider than a range across 2 groups, even when nothing real is going on.

## Limits
- Synthetic data. The category counts are nearly equal, which real shops rarely have
- Many Total, Quantity, and Price values were repaired by arithmetic, not observed originally
- Dates are partly missing, which limits time-based analysis

## Verdict
**NO-GO for predicting spend from Location, Payment Method, or weekday.**

NO-GO means I found no usable signal, not that no effect exists. With gaps this small, this data cannot tell a real effect from chance. The cleaning itself worked: 10,000 rows became 9,974, with only 26 dropped.