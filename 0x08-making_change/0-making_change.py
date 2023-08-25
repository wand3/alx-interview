#!/usr/bin/python3
"""
Making Change
"""


def makeChange(coins, total):
    """
    Return the minimum number of coins needed to meet a given total
    Args:
        coins (list of ints): a list of coins of different values
        total (int): total value to be met
    Return:
        Number of coins or -1 if meeting the total is not possible
    """
    if total < 1:
        return 0
    coins.sort()
    coins.reverse()
    fewestNumber = 0
    for coin in coins:
        if total <= 0:
            break
        buffer = total // coin
        fewestNumber += buffer
        total -= (buffer * coin)
    if total != 0:
        return -1
    return fewestNumber
