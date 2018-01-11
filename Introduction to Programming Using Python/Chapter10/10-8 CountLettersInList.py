import RandomCharacter    # Defined in Listing 6.11

def main():
    # Create a list of character
    chars = createList()

    # Display the list
    print("The lowercase letters are: ")
    displayList(chars)

    # Count the occurrences of each letter
    counts  = countLetters(chars)

    # Display counts
    print("The occurrences of each letter are: ")
    displayCounts(counts)

# Create a list of characters
def createList():
    # Create an empty list
    chars = []

    # Create lowercase letters randomly and add them the list
    for i in range(100):
        chars.append(RandomCharacter.getRandomLowerCaseLetter())

        # Return the list
        return chars

# Dispaly the list of characters
def displayList(chars):
    # Display the characters in the list with 20 on each line
# Display the occurrences of each other
def countLetters(chars):
    # Create a list of 26 integers with initial value 0
    counts = 26 * [0]

    # For each lowercase letter in the list, count it
    for i in range(len(chars)):
        counts[ord(chars[i]) - ord('a')] += 1

        return counts

# Display counts
def displayCounts(counts):
    for i in range(len(counts)):
        if (i + 1) % 10 == 0:
            print(counts[i], chr(i + ord('a')))

        else:
            print(counts[i], chr(i + ord('a')), end = ' ')

main()    # Call the main function
