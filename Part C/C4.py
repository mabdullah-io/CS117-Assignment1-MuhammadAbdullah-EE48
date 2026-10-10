# Loaded Voltage Divider

def loadedDivider(Vs, R1, R2, Rl):
  unloadedVoltage = Vs * (R2 / (R1 + R2))
  R_parallel = (R2 * Rl) / (R1 + R2)
  loadedVoltage = Vs * (R_parallel / (R1 + R_parallel))
  return round(unloadedVoltage, 1), round(loadedVoltage, 1)

vs = 12
r1 = 1000
r2 = 1000
rl = 500

result = loadedDivider(vs, r1, r2, rl)
print("Loaded Divider (Vs, R1, R2, Rl) => (12, 1000, 1000, 500):")
print("Unloaded Voltage =", loadedDivider(vs, r1, r2, rl)[0], "V")
print("Loaded Voltage =", loadedDivider(vs, r1, r2, rl)[1], "V")
