sum = 0
number = 0

while number < 20:
    number += 1
    if number == 10 or number == 11:
        continue    # continue语句只是退出循环的当前迭代
    sum += number

print("The sum is", sum)