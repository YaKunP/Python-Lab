def main():
    # Open file for output
    outfile = open("President.txt", "w")

    # Write data to the file
    outfile.write("Bill Clinton\n")
    outfile.write("George Bush\n")
    outfile.write("Brack Obama")

    outfile.close()    # Close the output file

main()    # Call the main function



'''
    当一个文件被打开来进行写操作或读操作时，一个被称为文件指针的特殊标记将会被放在文件内部。
    读或写操作在指针位置发生。当一个文件被打开时，文件指针被放在文件的起始位置。
    当对文件进行读或写操作时，文件指针将会前移
'''