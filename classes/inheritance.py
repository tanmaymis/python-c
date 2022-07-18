class Person:

    def __init__ (self,name,gender ="female"):
        self.name =name
        self.gender =gender

    def show(self):
        print("my details")
        print(f'name : {self.name}')
        print(f'gender : {self.gender}')


class student(Person):

    def __init__ (self,name,gender,klass,college,stream):
        super().__init__(name,gender)
        self.klass =klass
        self.college = college
        self.stream =stream

    def show_more(self):
        print("mmore details")
        print(f'college : {self.college}')
        print(f'klass : {self.klass}')
        print(f'stream : {self.stream}')

if __name__ == "__main__":
    P =Person("john cena" , gender ="Male")
    P.show()

    std1=student('ankit','male','python class' ,'digipodium', 'data analytics')
    std1.show()
    std1.show_more()

class coder(student):
    def __init__(self,name,gender,klass,college,stream,prog_langs =[]):
        super().__init__(name,gender,klass,college,stream)
        self.prglangs = prog_langs


    def coding_experince(self):
        if len(self.prglangs)==0:
            print(f'I,{self.name} dont know any programming language')
        else:
            print(f'I,{self.name} know following any programming language')
            for lang in self.prglangs:
                print(f' => {lang}')
            print('---' *10)

    def add_language(self,lang):
        self.prglangs.append(lang)

if __name__ == "__main__":
    P =Person("john cena" , gender ="Male")
    P.show()

    std1=student('ankit','male','python class' ,'digipodium', 'data science')
    std1.show()
    std1.show_more()

    coder =coder( 'tanmay mishra' , 'male' , '9th' , 'skd academy' ,'pcm')
    coder.show()
    coder.show_more()
    coder.coding_experince()
    print('ek saal bad')
    coder.add_language('python')
    coder.add_language('css')
    coder.add_language('html')
    coder.coding_experince()

