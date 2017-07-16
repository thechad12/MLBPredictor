import mlbgame
import pandas as pd

mdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months = [(month + 1) for month in range(12)]

home_team = []
away_team = []
home_errors = []
home_hits = []
home_runs = []
away_errors = []
away_hits = []
away_runs = []

def listDates(days):
	for day in days:
		d = range(day)
		return d

game_days = listDates(mdays)

for m in months:
	for g in game_days:
		games = mlbgame.day(2017,m,g)
		for game in games:
			try:
				home = game.home_team
				away = game.away_team
				home_e = game.home_team_errors
				home_h = game.home_team_hits
				home_r = game.home_team_runs
				away_e = game.away_team_errors
				away_h = game.away_team_hits
				away_r = game.away_team_runs
				home_team.append(home)
				home_errors.append(home_e)
				home_hits.append(home_h)
				home_runs.append(home_r)
				away_team.append(away)
				away_errors.append(away_e)
				away_hits.append(away_h)
				away_runs.append(away_r)
			except:
				continue
data = pd.DataFrame({
	'home_team': home_team,
	'home_errors': home_errors,
	'home_hits': home_hits,
	'home_runs': home_runs,
	'away_team': away_team,
	'away_errors': away_errors,
	'away_hits': away_hits,
	'away_runs': away_runs
	})

data.to_csv('output.csv')

