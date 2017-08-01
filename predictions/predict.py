import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import random
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
import os
from sklearn.linear_model import LinearRegression
import mlbgame

csv = open(os.path.join(os.path.dirname(__file__), os.pardir, 'output.csv'))

train = pd.read_csv(csv)

ID_col = train['home_team']
target_col = train['home_runs']

