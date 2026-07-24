"""Day 8:Numpy random """
import numpy as np
np.random.seed(50)
print(np.random.rand(5))
# When i run it twice it gives same output [0.49460165 0.2280831  0.25547392 0.39632991 0.3773151 ] becuase we have set the seed
# If we run it different times without seed  it will  generate different numbers evrytime but with seed it generates same numbers
print(np.random.randint(1,100,5))
A = np.random.randn(5)
print(A)
print(A.mean())
# my actual mean came out to -0.8602339392031524 — not exactly 0, because
# 5 samples is a small, noisy estimate. mean() is just sum()/count (Day 5) —
# with only 5 values, the random luck of which side of the bell curve got sampled
# more heavily still shows through. With hundreds/thousands of samples instead,
# positives and negatives cancel out more evenly and the mean converges closer to 0.