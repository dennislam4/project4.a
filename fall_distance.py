# Author: Dennis Lam
# GitHub username: dennislam4
# Date: 7/05/2022
# Description: A function that determines the distance an object falls due to gravity in a specific time period.

gravity = 9.8


def fall_distance(time):
    """Takes in time as a number value and calculates object fall distance by converting time into distance in meters"""
    dist = ((1 / 2) * gravity * time ** 2)
    return dist
