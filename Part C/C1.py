# Current and Power calculation using functions

def calculateCurrent(V, R):
  I = V / R
  return I

def calculatePower(V, R):
  I = calculateCurrent(V, R)
  P = (I ** 2) * R
  return P

v = 12
r = 6

print("Current =", calculateCurrent(v, r), "A")
print("Power =", calculatePower(v, r), "W")
