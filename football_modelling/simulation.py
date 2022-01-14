import pandas as pd
import numpy as np
from scipy.stats import poisson


def simulate_match(foot_model, homeTeam, awayTeam, max_goals=10):

    home_goals_avg = foot_model.predict(
        pd.DataFrame(
            data={"team": homeTeam, "opponent": awayTeam, "home": 1}, index=[1]
        )
    ).values[0]
    away_goals_avg = foot_model.predict(
        pd.DataFrame(
            data={"team": awayTeam, "opponent": homeTeam, "home": 0}, index=[1]
        )
    ).values[0]
    team_pred = [
        [poisson.pmf(i, team_avg) for i in range(0, max_goals + 1)]
        for team_avg in [home_goals_avg, away_goals_avg]
    ]
    return np.outer(np.array(team_pred[0]), np.array(team_pred[1]))
