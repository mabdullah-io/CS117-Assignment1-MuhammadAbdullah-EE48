# Converts resistances from a Star to the equivalent Delta network

def starToDelta(Ra, Rb, Rc):
  R_numerator = (Ra * Rb) + (Rb * Rc) + (Rc * Ra)

  R_ab = round(R_numerator / Rc, 2)
  R_bc = round(R_numerator / Ra, 2)
  R_ca = round(R_numerator / Rb, 2)

  return (R_ab, R_bc, R_ca)

print("Star to Delta (10, 20, 30) =", starToDelta(10, 20, 30))
