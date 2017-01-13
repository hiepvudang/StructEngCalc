import simply

print('What type of beams? \n1. Simply supported, 2. Cantilever, 3. Fixed')
bIn1 = int(input())

print('What type of loads? \n1. UDL, 2. Point load at mid-span')
bIn2 = int(input())

print('What type of material? \n1. Concrete, 2. Steel')
bIn3 = int(input())

if bIn2 == 1:
    print('What is the value of load? [kN/m]')
else:
    print('What is the point load? [kN]')
bIn2a = float(input())

print('What is the span length? [m]')
bIn4 = float(input())

a = simply
b = 'udl'

moment, shear = getattr(a, b)(bIn2a, bIn4)

print('Moment = ' + moment + '[kNm]')
print('Shear = ' + shear + '[kN]')

