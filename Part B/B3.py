# Finding highest, lowest, average and readings above 3.2V

readings = (3.3, 3.1, 3.4, 2.9, 3.6, 3.0, 3.2)

total = 0
highest = readings[0]
lowest = readings[0]
count = 0;

for val in readings:
  total += val
  if (val > highest):
    highest = val
  if (val < lowest):
    lowest = val
  if (val > 3.2):
    count += 1

print("Readings above 3.2 V:", count)
print("Highest:", highest, "V")
print("Lowest:", lowest, "V")
print("Average:", round(total / len(readings), 2), "V")
