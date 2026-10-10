# Finding the longest consecutive streak of voltage drops in a Battery management system

voltages = [12.6, 12.5, 12.5, 12.3, 12.1, 11.9, 12.0, 11.8, 11.6, 11.5, 11.5, 11.2]

maxLen = 1
start = voltages[0]
end = voltages[0]

tempLen = 1
tempStart = voltages[0]

for i in range(1, len(voltages)):

  if (voltages[i] < voltages[i - 1]):
    tempLen += 1
  else:
    if (tempLen > maxLen):
      maxLen = tempLen
      start = tempStart
      end = voltages[i - 1]
    tempLen = 1
    tempStart = voltages[i]

if (tempLen > maxLen):
  maxLen = tempLen
  start = tempStart
  end = voltages[-1]

print("Longest continuous drop:", maxLen, "minutes")
print("Started at:", start, "V")
print("Ended at:", end, "V")
