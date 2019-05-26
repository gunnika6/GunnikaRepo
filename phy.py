#!/usr/bin/env python
import pandas as pd
import numpy as np
df=pd.read_csv("flightdelays.csv")
x=df[df["Origin"]== "SFO"]["ArrDelay"].head(3)
x.to_csv("first3sfo.csv")
y=pd.read_csv("first3sfo.csv",header=None)[1]
print(y)
a=df["Dest"].value_counts().head(3)
print(a)


