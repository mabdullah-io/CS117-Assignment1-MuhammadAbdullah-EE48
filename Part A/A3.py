# Resistor color band digit checker

color = input("Enter band color: ").lower()
digit = -1

if (color == "black"):
  digit = 0
elif (color == "brown"):
  digit = 1
elif (color == "red"):
  digit = 2
elif (color == "orange"):
  digit = 3
elif (color == "yellow"):
  digit = 4
elif (color == "green"):
  digit = 5
elif (color == "blue"):
  digit = 6
elif (color == "violet"):
  digit = 7
elif (color == "grey"):
  digit = 8
elif (color == "white"):
  digit = 9

if (digit >= 0):
  print("Digit =", digit)
else:
  print("Invalid color")
