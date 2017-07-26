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
z = df['home_errors']

model_hits = sm.OLS(y, x).fit()
predict_hits = model_hits.predict(x)

pred_hits = model_hits.summary()

model_errors = sm.OLS(z, x).fit()
predict_errors = model_hits.predict(x)

pred_errors = model_errors.summary()

print(pred_hits)
print(pred_errors)