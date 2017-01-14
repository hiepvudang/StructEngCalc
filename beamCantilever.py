"""
Date: 170112
Write formula for cantilever beam: one end is fixed and the other is free end.
"""


def udl(load, span, stiffness):
    # Formula for Uniform Distributed Load
    bending_moment = load * span ** 2 / 2
    shear = load * span
    deflection = load * (span * 1e3) ** 4 / (8 * stiffness)
    return bending_moment, shear, deflection


def point_load(load, span, stiffness):
    # Formula for Point Load at free end
    bending_moment = load * span
    shear = load
    deflection = load * (span * 1e3) ** 3 / (3 * stiffness)
    return bending_moment, shear, deflection
