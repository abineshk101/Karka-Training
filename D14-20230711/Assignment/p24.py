def area_triangle(a,b,c):
    s=(a+b+c)/2
    area=(s*(s-a)*(s-b)*(s-c))**0.5
    return area
print("Areaof TRIANGLE")
a=int(input("Enter the side1 value of trirangle "))
b=int(input("Enter the side2 value trirangle "))
c=float(input("enter the side3 value trirangle "))
print("The area is ",area_triangle(a,b,c),"\n")

def area_sqr(s):
    area=a**2
    return area
print("Area of SQUARE ")
s=int(input("Enter the side value of square "))
print("The area of square is ",area_sqr(s),"\n")

def area_rct(l,b):
    area=l*b
    return area
print("Area of RECTANGLE ")
l=int(input("Enter the length of rectangle "))
b=int(input("Enter the breadth of recangle "))
print("The area of rectangle is ",area_rct(l,b),"\n")

def area_circle(r):
    area=3.14*(r)**2
    return area
print("Area of CIRCLE")
r=int(input("Enter the radius "))
print("The ara of circle is ",area_circle(r),"\n")

def area_trap(a,b,h):
    area=((a+b)/2)*h
    return area
print("Area of TRAPEZIUM")
a=int(input("Enter the value of base1 "))
b=int(input("Enter the value of base2 "))
h=int(input("Ente the value of height "))
print("Th area of Trapezium is ",area_trap(a,b,h))