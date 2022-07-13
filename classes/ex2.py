#constructor

class Paratha:
    def __init__(self,typ,price):
        self.type =typ #object variable
        self.price =price

    def display(self):
        print(f"{self.type} : {self.price}")

if __name__ == "__main__":
    ap =Paratha("Aloo Paratha",30)
    bp =Paratha("Panner Paratha",50)
    pp =Paratha("pyaaz Paratha",40)
    mp =Paratha("Muli Paratha",20)

    print("Todays Menu")
    ap.display()
    bp.display()
    pp.display()
    mp.display()