# Prompt the user for input
seconds = eval(input("Enter an integer for seconds: "))

# Get minutes and remaining seconds
minutes = seconds // 60     # Find minutes in seconds
remainingSeconds = seconds % 60    # Seconds remaining
print(seconds, "seconds is", minutes, "minutes and", remainingSeconds, "seconds")



'''
    Note:
        浮点数：在内存中以科学计数法存储
        
        当一个变量被赋值一个太大的值而不能存入内存中，就会导致数据溢出
        
        int和eval区别：
            两个函数都将字符串转换为整型；
            int函数完成一个简单的转换，它不能用于非整型字符串
            eval有一个微妙的疑难杂症，如果数字串前有先导零会使eval产生错误，相对地，int函数可以很好处理这个问题
            
'''