def area_of_triangle():
    a =int(input("enter the length of side a: "))
    b =int(input("enter the length of side b: "))
    c =int(input("enter the length of side b: "))
    s=(a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c))**0.5
    print("the area of triangle is :" , area)

def area_of_circle():
    r = int(input("enter the radius of circle : "))
    area = 3.14*r**2
    print("the area of circle is : " , area)

def area_of_rectangle():
    l = int(input("enter the length of the rectangle : "))
    b = int(input("enter the breadth of the rectangle : "))
    area = l*b
    print("the area of rectangle is : " , area)

def menu():
    print("1 : Area of triangle")
    print("2 : Area of circle")
    print("3 : Area of rectangle") 
    print("4 : Quit")
    choice = int(input("enter your choice : "))   
    if choice == 1:
        area_of_triangle()
    elif choice == 2:
        area_of_circle()
    elif choice == 3:
        area_of_rectangle()
    elif choice == 4:
        print("goodbye")
    else:
        print("invalid choice")
        menu()

if __name__  == "__main__":
    menu()