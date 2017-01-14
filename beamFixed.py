"""
Date: 170112
Write formula for fixed-end beams
"""


def udl(load, span, stiffness):
    # Formula for Uniform Distributed Load
    bending_moment = load * span ** 2 / 12
    shear = load * span / 2
    deflection = load * (span * 1e3) ** 4 / (384 * stiffness)
    return bending_moment, shear, deflection


def point_load(load, span, stiffness):
    # Formula for Point Load at mid-span
    bending_moment = load * span / 8
    shear = load / 2
    deflection = load * (span * 1e3) ** 3 / (192 * stiffness)
    return bending_moment, shear, deflection
