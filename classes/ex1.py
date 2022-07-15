class Fan:   #properties
    brand ='Orient'
    blade_size =1200
    rpm=380

    def start(self,speed=1):  #function in a class    #star is method
        print(f'Fan is starting at {speed} speed')

if __name__ == "__main__":
    f= Fan()
    g=Fan()

    f.start(2)
    g.start(3)
    print(f.blade_size , g.blade_size)
    print(f.rpm , g.rpm)
    print(f.brand , g.brand)
    f.brand = "usha"
    f.blade_size = 1000
    f.rpm =400
    print(f.blade_size , g.blade_size)
    print(f.rpm , g.rpm)
    print(f.brand , g.brand)

