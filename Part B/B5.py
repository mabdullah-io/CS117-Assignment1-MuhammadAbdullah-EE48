# Sorting of 100 ohm resistors by checking tolerance

p1Count = 0
p5Count = 0
rejectCount = 0

while True:
  resistance = float(input("Enter measured resistance (0 to stop): "))
  if resistance == 0:
    break

  if (99.0 <= resistance <= 101.0):
    p1Count += 1
  elif (95.0 <= resistance <= 105.0):
    p5Count += 1
  else:
    rejectCount += 1

print("1% tolerance count:", p1Count)
print("5% tolerance count:", p5Count)
print("Rejected count:", rejectCount)
