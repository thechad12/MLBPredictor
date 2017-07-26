from sklearn import linear_model
from sklearn import datasets
import pandas as pd
import os
import statsmodels.api as sm

f = open(os.path.join(os.path.dirname(__file__), os.pardir, 'output.csv'))

data = pd.read_csv(f)

df = pd.DataFrame(data)

target = pd.DataFrame(data, columns=['home_runs'])

x = df['home_hits']
y = target['home_runs']

model = sm.OLS(y, x).fit()
predict = model.predict(x)

pred = model.summary()
print(pred)