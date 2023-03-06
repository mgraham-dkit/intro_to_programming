def slope(a, b):
    # Short approach:
    #x_val = b[0]-a[0]
    #y_val = b[1]-a[1]
    #slope = y_val/x_val
    
    # More explicit approach:
    x1 = a[0]
    x2 = b[0]
    y1 = a[1]
    y2 = b[1]
    
    x_val = x2-x1
    y_val = y2-y1
    slope = y_val/x_val
    
    return slope


x1 = int(input("Please enter the x position for the first coordinate: "))
y1 = int(input("Please enter the y position for the first coordinate: "))
a = (x1, y1)
x2 = int(input("Please enter the x position for the second coordinate: "))
y2 = int(input("Please enter the y position for the second coordinate: "))
b = (x2, y2)
print("The slope of the line between " + str(a) + " and " + str(b) + " = " + str(slope(a, b)))