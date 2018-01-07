# Initialize sum
'''
sum =  0

# Add 0.01, 0.02,  ..., 0.09, 1 to sum
i = 0.01
while i <= 1.0:
    sum += i
    i = i + 0.01

# Display result
print("The sum is", sum)

'''

sum = 0

count = 0
i = 0.01
while count < 100:
    sum += i
    i = i + 0.01
    count += 1

print("The sum is", sum)