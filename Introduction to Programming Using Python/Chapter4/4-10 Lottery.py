import random

# Generate a lottery number
lottery = random.randint(0, 99)

# Prompt the user to enter a guess
guess = eval(input("Enter your lottery pick (two digits): "))

# Get digits from lottery
lotteryDigitl = lottery // 10
lotteryDigit2 = lottery % 10

# Get digits from guess
guessDigit1 = guess // 10
guessDigit2 = guess % 10

print("The lottery number is", lottery)

# Check the guess
if guess == lottery:    # 检测guess数字是否和彩票数字完全匹配
    print("Exact match: you win $10,000")
elif (guessDigit2 == lotteryDigitl and guessDigit1 == lotteryDigit2):    # 如果不是，检测数字的逆序是否和彩票数字完全匹配
    print("Match all digits: you win $3,000")
elif (guessDigit1 == lotteryDigitl    # 如果不是，检测guess数字中的一个数是否和guess中的一个数字相同
      or guessDigit1 == lotteryDigit2
      or guessDigit2 == lotteryDigitl
      or guessDigit2 == lotteryDigit2):
    print("Match one digit: you win $1,000")

else:    # 如果不是，不匹配任何内容
    print("Sorry, no match")