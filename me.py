# Sum all multiples of 5 from 0 to 100 (0, 5, 10, ..., 100)

total = 0
for i in range(0, 101, 5):
    print(i)
    total += i

print("Sum of the numbers is", total)
