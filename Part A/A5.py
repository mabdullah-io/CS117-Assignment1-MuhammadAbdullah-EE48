# Finding smallest and largest resistors

R1 = int(input("Enter R1: "))
R2 = int(input("Enter R2: "))
R3 = int(input("Enter R3: "))

smallest = 0;
largest = 0;

if (R1 < R2 and R1 < R3):
  smallest = R1
elif (R2 < R1 and R2 < R3):
  smallest = R2
else:
  smallest = R3

if (R1 > R2 and R1 > R3):
  largest = R1
elif (R2 > R1 and R2 > R3):
  largest = R2
else:
  largest = R3

print("Smallest =", smallest, "ohm")
print("Largest =", largest, "ohm")
