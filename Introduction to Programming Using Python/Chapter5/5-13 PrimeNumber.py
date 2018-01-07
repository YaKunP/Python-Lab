'''
Set the number of prime numbers to be displayed as a constant NUMBER_OF_PRIMES
Use count to track the number of prime numbers and set an initial count to 0
Set an initial number to 2

while count < NUMBER_OF_PRIMES:
    Test if number is prime

    if number is prime:
        Display the prime number and increase count

    Increment number by 1


Use a Boolean variable isPrime to denote whether the number is prime; Set inPrime to True initially

for divisor in range(2, number / 2 + 1):
    set isPrime to False
    Exit the loop

'''

NUMBER_OF_PRIMES = 50    # Number of primes to display
NUMBER_OF_PRIMES_PER_LINE = 10    # Display 10 per line
count = 0    # Count the number of prime numbers
number = 2    # A number to be tested for primeness

print("The first 50 prime numbers are")

# Repeatedly find prime numbers
while count < NUMBER_OF_PRIMES:
    # Assume the number is prime
    isPrime = True    # Is the current number prime?

    # Test if number is prime
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            # If true, the number is not prime
            isPrime = False    # Set isPrime to false
            break    # Exit the for loop
        divisor += 1

    # Display the prime number and increase the count
    if isPrime:
        count += 1    # Increase the count

        print(format(number, "5d"), end = '')
        if count % NUMBER_OF_PRIMES_PER_LINE == 0:
            # Display the number and advance to the new line
            print()    # Jump to the new line

    # Check if the next number is prime

