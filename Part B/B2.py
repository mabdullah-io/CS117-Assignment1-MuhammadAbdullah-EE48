# Finding total resistance in series

resistorsCount = int(input("How many resistors? "))
totalResistance = 0

for r in range(1, resistorsCount + 1):
  print("For R", r, ":")
  totalResistance += int(input("Enter resistance (ohm): " ))

print("Total resistance =", totalResistance, "ohm")
