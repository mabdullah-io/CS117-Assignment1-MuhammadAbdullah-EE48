# Calculate Parallel resistance combination

def parallel(resistors):
  totalConductance = 0
  for r in resistors:
    totalConductance += 1 / r
  return round(1 / totalConductance, 2)

print("Parallel resistance (10, 10) =", parallel([10, 10]), "ohm")
print("Parallel resistance (100, 200, 300) =", parallel([100, 200, 300]), "ohm")
