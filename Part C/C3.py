# Decimal to Binary converter

def decimalToBinary(n):
  if n == 0:
    return "0"

  binary = ""
  while n > 0:
    binary = str(n % 2) + binary
    n = n // 2
  return binary

print("Decimal to Binary (10) =", decimalToBinary(10))
print("Decimal to Binary (25) =", decimalToBinary(25))
