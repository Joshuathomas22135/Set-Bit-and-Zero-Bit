n = 12
bit = 1
print("Setting a Bit")
n = n | (1<< bit)
print(n)

print("Clearing a Bit")
n = n & ~(1<<bit)
print(n)