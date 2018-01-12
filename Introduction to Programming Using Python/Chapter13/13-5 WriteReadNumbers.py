from random import randint

def main():
    # Open file for writing data
    outfile = open("Numbers.txt", "w")
    for i in range(10):
        outfile.write(str(randint(0, 9)) + " ")    # 为了向一个文件写入数字，必须首先将它们转换成字符串
    outfile.close()    # Close the file

    # Open file for reading data
    infile = open("Numbers.txt", "r")
    s = infile.read()
    numbers = [eval(x) for x in s.split()]
    for number in numbers:
        print(number, end = " ")
    infile.close()    # Close the file

main()    # Call the main function

