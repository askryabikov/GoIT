# Task 3 — Substring search benchmark (BM vs KMP vs RK)

## Setup
- Texts: `article1.txt`, `article2.txt`
- Text sizes: article1 ≈ 11129 chars, article2 ≈ 17590 chars
- Existing patterns:
  - Article 1: "Алгоритми"
  - Article 2: "Рекомендаційні системи"
- Non-existing pattern: generated string (guaranteed absent in both texts):
    base="хахахахахаха", appended with suffix until it’s absent in both texts
- Measurement: `timeit.repeat`, result = `min(times)/number` seconds per call

## Results
Paste your console output here (seconds per call):

- Article 1 | existing: BM=0.000043, KMP=0.000146, RK=0.000348
- Article 1 | non_existing: BM=0.000513, KMP=0.001882, RK=0.004396
- Article 2 | existing: BM=0.000108, KMP=0.000388, RK=0.000909
- Article 2 | non_existing: BM=0.000741, KMP=0.002681, RK=0.006353

## Fastest algorithm per text
- Article 1:
  - existing: BM
  - non_existing: BM

- Article 2:
  - existing: BM
  - non_existing: BM

Boyer–Moore wins here because it compares from the end of the pattern and performs larger 
shifts on mismatches, reducing comparisons on long texts

## Overall conclusion
- Fastest overall (across both texts and both pattern types): Boyer-Moore BM is fastest
here likely due to larger shifts (fewer comparisons), especially noticeable for 
non-existing patterns
- Notes:
  - Results can vary slightly due to OS/background load and Python runtime.
  - Non-existing search often takes longer because algorithms scan more of the text before failing.