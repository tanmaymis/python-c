def area_of_triangle(a,b,c):
    s = (a+b+c)/2
    area = (s*(s-a) * (s-b) *(s-c))**0.5
    return area

def area_of_circle(r):
    area =3.14*r**2
    return area

def area_of_rectangle(l,b):
    area = l*b
    return area

if __name__ == "__main__":
    r=6
    l=10
    b=15
    area2 = area_of_circle(r)
    area3 = area_of_rectangle(l,b)
    area4 = area_of_triangle(4,5,6)
    print(f'area of triangle {area4}')
    print(f'area of circle {area2}')
    print(f'area of rectangle {area3}')
