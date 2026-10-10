# Logic gates values for 2 bits

a = int(input("Enter A: "))
b = int(input("Enter B: "))

if ((a == 0 or a == 1) and (b == 0 or b == 1)):
  print("AND =", int(a and b))
  print("OR =", int(a or b))
  print("XOR =", int(a ^ b))
else:
  print("Bits must be 0 or 1")
