#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 17:32:00 2020

@author: davsu428
"""
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
from plotly import graph_objects, offline
import random


def createPitch(length, width, unity, linecolor):  # in meters
    # Code by @JPJ_dejong

    """
    creates a plot in which the 'length' is the length of the pitch (goal to goal).
    And 'width' is the width of the pitch (sideline to sideline).
    Fill in the unity in meters or in yards.

    """
    # Set unity
    if unity == "meters":
        # Set boundaries
        if length >= 120.5 or width >= 75.5:
            return str(
                "Field dimensions are too big for meters as unity, didn't you mean yards as unity?\
                       Otherwise the maximum length is 120 meters and the maximum width is 75 meters. Please try again"
            )
        # Run program if unity and boundaries are accepted
        else:
            # Create figure
            fig = plt.figure()
            # fig.set_size_inches(7, 5)
            ax = fig.add_subplot(1, 1, 1)

            # Pitch Outline & Centre Line
            plt.plot([0, 0], [0, width], color=linecolor)
            plt.plot([0, length], [width, width], color=linecolor)
            plt.plot([length, length], [width, 0], color=linecolor)
            plt.plot([length, 0], [0, 0], color=linecolor)
            plt.plot([length / 2, length / 2], [0, width], color=linecolor)

            # Left Penalty Area
            plt.plot(
                [16.5, 16.5], [(width / 2 + 16.5), (width / 2 - 16.5)], color=linecolor
            )
            plt.plot(
                [0, 16.5], [(width / 2 + 16.5), (width / 2 + 16.5)], color=linecolor
            )
            plt.plot(
                [16.5, 0], [(width / 2 - 16.5), (width / 2 - 16.5)], color=linecolor
            )

            # Right Penalty Area
            plt.plot(
                [(length - 16.5), length],
                [(width / 2 + 16.5), (width / 2 + 16.5)],
                color=linecolor,
            )
            plt.plot(
                [(length - 16.5), (length - 16.5)],
                [(width / 2 + 16.5), (width / 2 - 16.5)],
                color=linecolor,
            )
            plt.plot(
                [(length - 16.5), length],
                [(width / 2 - 16.5), (width / 2 - 16.5)],
                color=linecolor,
            )

            # Left 5-meters Box
            plt.plot(
                [0, 5.5],
                [(width / 2 + 7.32 / 2 + 5.5), (width / 2 + 7.32 / 2 + 5.5)],
                color=linecolor,
            )
            plt.plot(
                [5.5, 5.5],
                [(width / 2 + 7.32 / 2 + 5.5), (width / 2 - 7.32 / 2 - 5.5)],
                color=linecolor,
            )
            plt.plot(
                [5.5, 0.5],
                [(width / 2 - 7.32 / 2 - 5.5), (width / 2 - 7.32 / 2 - 5.5)],
                color=linecolor,
            )

            # Right 5 -eters Box
            plt.plot(
                [length, length - 5.5],
                [(width / 2 + 7.32 / 2 + 5.5), (width / 2 + 7.32 / 2 + 5.5)],
                color=linecolor,
            )
            plt.plot(
                [length - 5.5, length - 5.5],
                [(width / 2 + 7.32 / 2 + 5.5), width / 2 - 7.32 / 2 - 5.5],
                color=linecolor,
            )
            plt.plot(
                [length - 5.5, length],
                [width / 2 - 7.32 / 2 - 5.5, width / 2 - 7.32 / 2 - 5.5],
                color=linecolor,
            )

            # Prepare Circles
            centreCircle = plt.Circle(
                (length / 2, width / 2), 9.15, color=linecolor, fill=False
            )
            centreSpot = plt.Circle((length / 2, width / 2), 0.8, color=linecolor)
            leftPenSpot = plt.Circle((11, width / 2), 0.8, color=linecolor)
            rightPenSpot = plt.Circle((length - 11, width / 2), 0.8, color=linecolor)

            # Draw Circles
            ax.add_patch(centreCircle)
            ax.add_patch(centreSpot)
            ax.add_patch(leftPenSpot)
            ax.add_patch(rightPenSpot)

            # Prepare Arcs
            leftArc = Arc(
                (11, width / 2),
                height=18.3,
                width=18.3,
                angle=0,
                theta1=308,
                theta2=52,
                color=linecolor,
            )
            rightArc = Arc(
                (length - 11, width / 2),
                height=18.3,
                width=18.3,
                angle=0,
                theta1=128,
                theta2=232,
                color=linecolor,
            )

            # Draw Arcs
            ax.add_patch(leftArc)
            ax.add_patch(rightArc)
            # Axis titles

    # check unity again
    elif unity == "yards":
        # check boundaries again
        if length <= 95:
            return str("Didn't you mean meters as unity?")
        elif length >= 131 or width >= 101:
            return str(
                "Field dimensions are too big. Maximum length is 130, maximum width is 100"
            )
        # Run program if unity and boundaries are accepted
        else:
            # Create figure
            fig = plt.figure()
            # fig.set_size_inches(7, 5)
            ax = fig.add_subplot(1, 1, 1)

            # Pitch Outline & Centre Line
            plt.plot([0, 0], [0, width], color=linecolor)
            plt.plot([0, length], [width, width], color=linecolor)
            plt.plot([length, length], [width, 0], color=linecolor)
            plt.plot([length, 0], [0, 0], color=linecolor)
            plt.plot([length / 2, length / 2], [0, width], color=linecolor)

            # Left Penalty Area
            plt.plot([18, 18], [(width / 2 + 18), (width / 2 - 18)], color=linecolor)
            plt.plot([0, 18], [(width / 2 + 18), (width / 2 + 18)], color=linecolor)
            plt.plot([18, 0], [(width / 2 - 18), (width / 2 - 18)], color=linecolor)

            # Right Penalty Area
            plt.plot(
                [(length - 18), length],
                [(width / 2 + 18), (width / 2 + 18)],
                color=linecolor,
            )
            plt.plot(
                [(length - 18), (length - 18)],
                [(width / 2 + 18), (width / 2 - 18)],
                color=linecolor,
            )
            plt.plot(
                [(length - 18), length],
                [(width / 2 - 18), (width / 2 - 18)],
                color=linecolor,
            )

            # Left 6-yard Box
            plt.plot(
                [0, 6],
                [(width / 2 + 7.32 / 2 + 6), (width / 2 + 7.32 / 2 + 6)],
                color=linecolor,
            )
            plt.plot(
                [6, 6],
                [(width / 2 + 7.32 / 2 + 6), (width / 2 - 7.32 / 2 - 6)],
                color=linecolor,
            )
            plt.plot(
                [6, 0],
                [(width / 2 - 7.32 / 2 - 6), (width / 2 - 7.32 / 2 - 6)],
                color=linecolor,
            )

            # Right 6-yard Box
            plt.plot(
                [length, length - 6],
                [(width / 2 + 7.32 / 2 + 6), (width / 2 + 7.32 / 2 + 6)],
                color=linecolor,
            )
            plt.plot(
                [length - 6, length - 6],
                [(width / 2 + 7.32 / 2 + 6), width / 2 - 7.32 / 2 - 6],
                color=linecolor,
            )
            plt.plot(
                [length - 6, length],
                [(width / 2 - 7.32 / 2 - 6), width / 2 - 7.32 / 2 - 6],
                color=linecolor,
            )

            # Prepare Circles; 10 yards distance. penalty on 12 yards
            centreCircle = plt.Circle(
                (length / 2, width / 2), 10, color=linecolor, fill=False
            )
            centreSpot = plt.Circle((length / 2, width / 2), 0.8, color=linecolor)
            leftPenSpot = plt.Circle((12, width / 2), 0.8, color=linecolor)
            rightPenSpot = plt.Circle((length - 12, width / 2), 0.8, color=linecolor)

            # Draw Circles
            ax.add_patch(centreCircle)
            ax.add_patch(centreSpot)
            ax.add_patch(leftPenSpot)
            ax.add_patch(rightPenSpot)

            # Prepare Arcs
            leftArc = Arc(
                (11, width / 2),
                height=20,
                width=20,
                angle=0,
                theta1=312,
                theta2=48,
                color=linecolor,
            )
            rightArc = Arc(
                (length - 11, width / 2),
                height=20,
                width=20,
                angle=0,
                theta1=130,
                theta2=230,
                color=linecolor,
            )

            # Draw Arcs
            ax.add_patch(leftArc)
            ax.add_patch(rightArc)

    # Tidy Axes
    plt.axis("off")

    return fig, ax


def createPitchOld():
    # Taken from FC Python
    # Create figure
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    # Pitch Outline & Centre Line
    plt.plot([0, 0], [0, 90], color=linecolor)
    plt.plot([0, 130], [90, 90], color=linecolor)
    plt.plot([130, 130], [90, 0], color=linecolor)
    plt.plot([130, 0], [0, 0], color=linecolor)
    plt.plot([65, 65], [0, 90], color=linecolor)

    # Left Penalty Area
    plt.plot([16.5, 16.5], [65, 25], color=linecolor)
    plt.plot([0, 16.5], [65, 65], color=linecolor)
    plt.plot([16.5, 0], [25, 25], color=linecolor)

    # Right Penalty Area
    plt.plot([130, 113.5], [65, 65], color=linecolor)
    plt.plot([113.5, 113.5], [65, 25], color=linecolor)
    plt.plot([113.5, 130], [25, 25], color=linecolor)

    # Left 6-yard Box
    plt.plot([0, 5.5], [54, 54], color=linecolor)
    plt.plot([5.5, 5.5], [54, 36], color=linecolor)
    plt.plot([5.5, 0.5], [36, 36], color=linecolor)

    # Right 6-yard Box
    plt.plot([130, 124.5], [54, 54], color=linecolor)
    plt.plot([124.5, 124.5], [54, 36], color=linecolor)
    plt.plot([124.5, 130], [36, 36], color=linecolor)

    # Prepare Circles
    centreCircle = plt.Circle((65, 45), 9.15, color=linecolor, fill=False)
    centreSpot = plt.Circle((65, 45), 0.8, color=linecolor)
    leftPenSpot = plt.Circle((11, 45), 0.8, color=linecolor)
    rightPenSpot = plt.Circle((119, 45), 0.8, color=linecolor)

    # Draw Circles
    ax.add_patch(centreCircle)
    ax.add_patch(centreSpot)
    ax.add_patch(leftPenSpot)
    ax.add_patch(rightPenSpot)

    # Prepare Arcs
    leftArc = Arc(
        (11, 45),
        height=18.3,
        width=18.3,
        angle=0,
        theta1=310,
        theta2=50,
        color=linecolor,
    )
    rightArc = Arc(
        (119, 45),
        height=18.3,
        width=18.3,
        angle=0,
        theta1=130,
        theta2=230,
        color=linecolor,
    )

    # Draw Arcs
    ax.add_patch(leftArc)
    ax.add_patch(rightArc)

    # Tidy Axes
    plt.axis("off")

    return fig, ax


def createGoalMouth():
    # Adopted from FC Python
    # Create figure
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    linecolor = "black"

    # Pitch Outline & Centre Line
    plt.plot([0, 65], [0, 0], color=linecolor)
    plt.plot([65, 65], [50, 0], color=linecolor)
    plt.plot([0, 0], [50, 0], color=linecolor)

    # Left Penalty Area
    plt.plot([12.5, 52.5], [16.5, 16.5], color=linecolor)
    plt.plot([52.5, 52.5], [16.5, 0], color=linecolor)
    plt.plot([12.5, 12.5], [0, 16.5], color=linecolor)

    # Left 6-yard Box
    plt.plot([41.5, 41.5], [5.5, 0], color=linecolor)
    plt.plot([23.5, 41.5], [5.5, 5.5], color=linecolor)
    plt.plot([23.5, 23.5], [0, 5.5], color=linecolor)

    # Goal
    plt.plot([41.5 - 5.34, 41.5 - 5.34], [-2, 0], color=linecolor)
    plt.plot([23.5 + 5.34, 41.5 - 5.34], [-2, -2], color=linecolor)
    plt.plot([23.5 + 5.34, 23.5 + 5.34], [0, -2], color=linecolor)

    # Prepare Circles
    leftPenSpot = plt.Circle((65 / 2, 11), 0.8, color=linecolor)

    # Draw Circles
    ax.add_patch(leftPenSpot)

    # Prepare Arcs
    leftArc = Arc(
        (32.5, 11),
        height=18.3,
        width=18.3,
        angle=0,
        theta1=38,
        theta2=142,
        color=linecolor,
    )

    # Draw Arcs
    ax.add_patch(leftArc)

    # Tidy Axes
    plt.axis("off")

    return fig, ax


class Field:
    def __init__(self):
        figure = graph_objects.Figure()

        figure.update_layout(
            width=900 * 1.388, height=900, autosize=False, plot_bgcolor="white"
        )
        figure.update_xaxes(range=[-0.03, 1.03])
        figure.update_yaxes(range=[-0.03, 1.03])

        self.figure = figure

        self.__draw_full()

    def add_title(self, main_title: str):
        """
        Adds a title to the pitch visualization
        """
        self.figure.update_layout(
            title={
                "text": main_title,
                "x": 0.48,
                "y": 0.91,
                "xanchor": "center",
                "yanchor": "top",
            }
        )

    def save(self, name: str):
        """Saves PNG and html image"""
        offline.plot(self.figure, filename=f"{name}", auto_open=False)

    def __draw_full(self):
        # Contour
        self.figure.add_shape(type="rect", x0=0, y0=0, x1=1, y1=1)
        # Half way line
        self.figure.add_shape(type="line", x0=0.5, y0=0, x1=0.5, y1=1)
        circle_radius = 0.0915
        self.figure.add_shape(
            type="circle",
            x0=0.5 - circle_radius * 0.72,
            y0=0.5 - circle_radius,
            x1=0.5 + circle_radius * 0.72,
            y1=0.5 + circle_radius,
        )
        # Defensive goal area
        self.figure.add_shape(type="rect", x0=0, y0=0.211, x1=0.170, y1=0.789)
        self.figure.add_shape(type="rect", x0=0, y0=0.368, x1=0.058, y1=0.632)
        self.figure.add_shape(type="rect", x0=-0.01, y0=0.447, x1=0.0, y1=0.553)
        # Attacking goal area
        self.figure.add_shape(type="rect", x0=0.83, y0=0.211, x1=1.0, y1=0.789)
        self.figure.add_shape(type="rect", x0=0.942, y0=0.368, x1=1.0, y1=0.632)
        self.figure.add_shape(type="rect", x0=1.0, y0=0.447, x1=1.01, y1=0.553)


def add_possession_chain_sb(figure, chain, team_name: str, opacity: int = 1.0):
    this_team_color = "#1F77B4"
    other_team_color = "#FF7F0E"

    chain_x = []
    chain_y = []
    text = []
    colors = []
    outcomes = []
    times = []
    counter = 0
    try:
        for idx, row in chain.iterrows():
            event_name = row["type_name"]
            event_loc = row["location"]

            # Transform  coordinates
            x = round((event_loc[0] * (100 / 120)) / 100, 3)
            y = round(
                ((80 - event_loc[1]) * (100 / 80)) / 100, 3
            )  # Reverse it because opta pitch is 0,100 and statsbomb 100,0

            color = this_team_color

            # slightly shift events that has the same coodinates
            if x in chain_x and y in chain_y:
                x = x + random.choice([-0.001, 0.001])
                y = y + random.choice([-0.001, 0.001])

            if row["possession_team_id"] != row["team_id"]:
                color = other_team_color
                x = round(1.000 - x, 3)
                y = round(1.000 - y, 3)

            chain_x.append(x)
            chain_y.append(y)
            if row["possession_team_id"] == row["team_id"]:
                text.append(f"{counter}.{event_name}")
            else:
                text.append(f"{counter}.{event_name}")

            colors.append(color)
            times.append(f"{row['minute']}{row['second']}")
            outcomes.append("circle")
            counter += 1

    except Exception as err:
        print(err)

    line_color = "#7F7F7F"

    figure.add_trace(
        {
            "mode": "markers+lines+text",
            "textposition": "top center",
            "type": "scatter",
            "x": chain_x,
            "y": chain_y,
            "hovertemplate": "Time: %{hovertext}<br>Event: %{text}",
            "text": text,
            "opacity": opacity,
            "hovertext": times,
            "marker": {"color": colors, "size": 8, "symbol": outcomes},
            "line": {"color": line_color, "dash": "solid"},
            "name": "{} {}:{} ".format(
                chain.iloc[0]["minute"], chain.iloc[0]["second"], team_name
            ),
        }
    )
