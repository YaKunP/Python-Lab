sum = 0
number = 0

while number < 20:
    number += 1
    sum += number
    if sum >= 100:
        break    # break语句跳出整个循环

print("The number is", number)
print("The sum is", sum)