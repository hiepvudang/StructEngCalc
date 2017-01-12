"""
Date: 170112
Write formula for simply supported bridge
"""


def udl(p, l):
    moment = p * l ** 2 / 8
    return moment
