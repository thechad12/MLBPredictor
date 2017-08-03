import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import random
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import linear_model
import os
from sklearn.linear_model import LinearRegression
import mlbgame
import datetime as dt
from datetime import date

csv = open(os.path.join(os.path.dirname(__file__), os.pardir, 'output.csv'))

train = pd.read_csv(csv)

today = dt.datetime.today()

games = mlbgame.day(today.year, today.month, today.day)
teams = []
for game in games:
	try:
		teams.append(game.home_team)
		teams.append(game.away_team)
	except:
		continue

ID_col = train['home_team']
target_col = train['home_runs']

for team in teams:
	run_predict = LinearRegression.predict(target_col)
	print(team + ":" + run_predict)


