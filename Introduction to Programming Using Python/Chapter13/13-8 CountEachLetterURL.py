import urllib.request
infile = urllib.request.urlopen("http://www.yahoo.com")    # 从网站上获取数据
print(infile.read().decode())
'''
def main():
    url = input("Enter a URL for a file: ").strip()
    infile = urllib.request.urlopen(url)
    s = infile.read().decode()    # Read the content as string

    counts = countLetters(s.lower())

    # Display results
    for i in range(len(counts)):
        if counts[i] != 0:
            print(chr(ord('a') + i) + " appears" + str(counts[i]) + (" time" if counts[i] == 1 else " times"))

# Count each letter in the string
def countLetters(s):
    counts = 26 * [0]    # Create an initialize counts
    for ch in s:
        if ch.isalpha():
            counts[ord(ch) - ord('a')] += 1
    return counts

main()    # Call the main function

'''