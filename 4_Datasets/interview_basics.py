#!/usr/bin/env python

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_parquet("interview_dataset.parquet")
df.describe()
df.hist()
plt.show()
