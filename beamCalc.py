# Date: 170114
# Write the first program to calculate moment, shear and deflection of a beam
import beamSimply           # Import the function to calculate simply supported structure
import sectionGeometry      # Import the function to calculate Section Properties of the section

# ----------------------------------------------------------------------------------------------------------------------
# Input the type of beam and span length
print('What type of beams? \n1. Simply supported, 2. Cantilever, 3. Fixed')
beam_select = int(input())
beam_list = {1: beamSimply, 2: beamCantilever, 3: beamFixed}
print('What is the span length [m]?')
span = float(input())

# Select load type and value
if beam_select != 2:
    print('What type of loads? \n1. UDL, 2. Point load at mid-span')
else:
    print('What type of loads? \n1. UDL, 2. Point load at free end')
load_select = int(input())
load_list = {1: 'udl', 2: 'point_load'}

if load_select == 1:
    print('What is the value of load [kN/m]?')
else:
    print('What is the point load [kN]?')
load = float(input())

# Choose the material and section geometry to calculate section properties
print('What type of material? \n1. Concrete, 2. Steel')
mat_type = int(input())
print('What is the section? \n1. Rectangle, 2. Circle')
sect_type = int(input())
# Find the section properties of the section
second_moment, stiffness = sectionGeometry.sectprop(sect_type, mat_type)

# Calculate the moment, shear and deflection
beam_type = beam_list[beam_select]
load_type = load_list[load_select]
moment, shear, deflection = getattr(beam_type, load_type)(load, span, stiffness)

# ----------------------------------------------------------------------------------------------------------------------
# Print the output
print('Moment = ', "%.2f" % round(moment, 2), '[kNm]')
print('Shear = ', "%.2f" % round(shear, 2), '[kN]')
print('Deflection = ', "%.2f" % round(deflection, 2), '[mm]')
