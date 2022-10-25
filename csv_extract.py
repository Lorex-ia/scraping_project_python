
# coding=utf-8
import pandas as pd

data = pd.read_csv("inpi.csv", sep=";", encoding="latin-1")
print(data)