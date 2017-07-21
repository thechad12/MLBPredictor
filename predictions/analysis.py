from sklearn import linear_model
import pandas as pd
import os

f = open(os.path.join(os.path.dirname(__file__), os.pardir, 'output.csv'))

data = pd.read_csv(f)

home_team = data['home_team']
home_errors = data['home_errors']
home_hits = data['home_hits']
home_runs = data['home_runs']
away_team = data['away_team']
away_hits = data['away_hits']
away_errors = data['away_errors']
away_runs = data['away_errors']


linear = linear_model.LinearRegression()

# Reshape data for consistency
hits = linear.fit(home_hits.reshape(len(home_hits),1),
	home_runs.reshape(len(home_runs),1))
errors = linear.fit(home_errors.reshape(len(home_errors),1),
	home_runs.reshape(len(home_runs),1))

sc_hits = linear.score(hits, home_runs)
sc_errors = linear.score(errors, home_runs)

