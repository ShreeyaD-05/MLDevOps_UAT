import numpy as np, pandas as pd

r = np.random.default_rng(42)
n = 200
pd.DataFrame({"age": r.normal(30, 5, n).round(1),
              "income": r.normal(50000, 8000, n).round(0),
              "score": r.normal(70, 10, n).round(1)}).to_csv("reference.csv", index=False)
pd.DataFrame({"age": r.normal(38, 5, n).round(1),
              "income": r.normal(62000, 8000, n).round(0),
              "score": r.normal(70, 10, n).round(1)}).to_csv("current.csv", index=False)