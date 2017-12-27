import turtle

# Prompt the user for inputting two points
x1, y1 = eval(input("Enter x1 and y1 for point 1: "))
x2, y2 = eval(input("Enter x2 and y2 for point 2: "))

# Compute the distance
distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# Display two points and the connecting line
turtle.penup()
turtle.goto(x1, y1)    # Move to (x1, y1)
turtle.pendown()
turtle.write("Point 1")
turtle.goto(x2, y2)    # Draw a line to (x2, y2)
turtle.write("Point 2")

# Move to the center point of the line
turtle.penup()
turtle.goto((x1 + x2) / 2, (y1 + y2) / 2)
turtle.write(distance)

turtle.done()



'''
    Note:
        1) 提示用户键入两个点
        2) 计算点之间的距离
        3) 利用Turtle图形显示两点间的连线
        4) 在线的中央显示线的长度
'''