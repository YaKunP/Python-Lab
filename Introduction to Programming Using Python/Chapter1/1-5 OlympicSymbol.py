import turtle    # 使用Turtle图形化窗口

turtle.color("blue")
turtle.penup()
turtle.goto(-110, -25)
turtle.pendown()
turtle.circle(45)

turtle.color("black")
turtle.penup()
turtle.goto(0, -25)
turtle.pendown()
turtle.circle(45)

turtle.color("red")
turtle.penup()
turtle.goto(110, -25)
turtle.pendown()
turtle.circle(45)

turtle.color("yellow")
turtle.penup()    # 抬起
turtle.goto(-55, -75)
turtle.pendown()    # 放下
turtle.circle(45)

turtle.color("green")
turtle.penup()
turtle.goto(55, -75)
turtle.pendown()
turtle.circle(45)    # Draw a circle with radius 45


turtle.done()    # 程序暂停，目的是给用户时间来查看图形




'''
    Note:
        Turtle是Python内嵌的绘制线、圆以及其他形状（包括文本）的图形模块
'''