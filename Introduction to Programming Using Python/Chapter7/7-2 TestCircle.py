from Circle import Circle

def main():
    # Create a circle with radius 1
    circle1 = Circle()
    print("The area of the circle of radius",
          circle.radius, "is", circle1.getArea())

    # Create a circle wirh radius 25
    circle2 = Circle(25)
    print("The area of the circle of radius",
          circle2.radius, "is", circle2.gerArea())

    # Create a circle with radius 125
    circle3 = Circle(125)
    print("The area of the circle of radius",
          circle3.radius, "is", circle3.getArea())

    # Modify circle radius
    circle2.radius = 100    # or circle2.setRadius(100)
    print("The area of the circle of radius",
          circle2.radius, "is", circle2.getArea())

main()    # Call the main function