import json
import pandas as pd
import numpy as np
from dotenv import load_dotenv, find_dotenv
import os
from pathlib import Path


##### STATSBOMB #####


def load_statsbomb_dir():
    load_dotenv(find_dotenv(), override=True)
    data_root_dir = Path(os.path.expanduser(os.getenv("DATA_ROOT_DIR")))
    statsbomb_subdir = os.getenv("STATSBOMB_DIR")
    statsbomb_dir = statsbomb_subdir = data_root_dir.joinpath(statsbomb_subdir)
    return statsbomb_dir


def load_wyscout_dir():
    load_dotenv(find_dotenv(), override=True)
    data_root_dir = Path(os.path.expanduser(os.getenv("DATA_ROOT_DIR")))
    wyscout_subdir = os.getenv("WYSCOUT_DIR")
    wyscout_dir = wyscout_dir = data_root_dir.joinpath(wyscout_subdir)
    return wyscout_dir


def load_statsbomb_competitions():
    statsbomb_dir = load_statsbomb_dir()

    competitions_file = statsbomb_dir.joinpath("competitions.json")

    with open(competitions_file, "rb") as f:
        competitions = json.load(f)
    return competitions


##### WYSCOUT #####


def load_wyscout_match_data(country="England", raw=False):
    """[summary]

    Args:
        country (str, optional): [description]. Defaults to "England".
        raw (bool, optional): [description]. Defaults to False.

    Returns:
        [type]: [description]
    """
    wyscout_dir = load_wyscout_dir()
    match_file = f"events_{country}.json"
    match_path = wyscout_dir.joinpath(match_file)
    with open(match_path) as f:
        data = json.load(f)
        train = pd.DataFrame(data)
    if raw:
        return train
    else:
        return preprocess_match_data(train)


def preprocess_match_data(train):
    """[summary]

    Args:
        train ([type]): [description]

    Returns:
        [type]: [description]
    """
    # check which unique sub-events there are to get the correct indicator of shots
    pd.unique(train["subEventName"])
    # select only shots
    shots = train[train["subEventName"] == "Shot"]
    # select outcome and
    shots_model = pd.DataFrame(columns=["Goal", "X", "Y"])
    shots_model
    for i, shot in shots.iterrows():

        header = 0
        for shottags in shot["tags"]:
            if shottags["id"] == 403:
                header = 1
        # Only include non-headers
        if not (header):
            shots_model.at[i, "X"] = 100 - shot["positions"][0]["x"]
            shots_model.at[i, "Y"] = shot["positions"][0]["y"]
            shots_model.at[i, "C"] = abs(shot["positions"][0]["y"] - 50)

            # Distance in metres and shot angle in radians.
            x = shots_model.at[i, "X"] * 105 / 100
            y = shots_model.at[i, "C"] * 65 / 100
            shots_model.at[i, "Distance"] = np.sqrt(x ** 2 + y ** 2)
            a = np.arctan(7.32 * x / (x ** 2 + y ** 2 - (7.32 / 2) ** 2))
            if a < 0:
                a = np.pi + a
            shots_model.at[i, "Angle"] = a

            # Was it a goal
            shots_model.at[i, "Goal"] = 0
            for shottags in shot["tags"]:
                # Tags contain that its a goal
                if shottags["id"] == 101:
                    shots_model.at[i, "Goal"] = 1
    for col in ["X", "Y"]:
        shots_model[col] = shots_model[col].astype("int")
    return shots_model
