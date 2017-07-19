from sklearn import linear_model
import pandas as pd

data = pd.read_csv('./output.csv')

home_team = data['home_team']
home_errors = data['home_errors']
home_hits = data['home_hits']
home_runs = data['home_runs']
away_team = data['away_team']
away_hits = data['away_hits']
away_errors = data['away_errors']
away_runs = data['away_errors']

linear = linear_model.LinearRegression()
hits = linear.fit(home_hits, home_runs)
errors = linear.fit(home_errors, home_runs)

sc_hits = linear.score(home_hits, home_runs)
sc_errors = linear.score(home_errors, home_runs)

