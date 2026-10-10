# Fuse safety checker using ohm's law

voltage = int(input("Enter voltage (V): "))
resistance = int(input("Enter resistance (ohm): "))

if (resistance > 0):

  current = voltage / resistance
  print("Current =", current, "A")

  if (current <= 2):
    print("Circuit is safe")
  else:
    print("Fuse will blow")

else:
  print("Invalid resistance")
