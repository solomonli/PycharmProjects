'''
class Robot:

    def __init__(self, name=None):
        self.name = name

    def say_hi(self):
        if self.name:
            print("Hi, I am " + self.name)
        else:
            print("Hi, I am a robot without a name")

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name


x = Robot()
x.set_name("Henry")
x.say_hi()
y = Robot()
y.set_name(x.get_name())
print(y.get_name())
print(Robot.__dict__)
'''


class Robot:
 
    def __init__(self, name=None, build_year=2000):
        self.__name = name
        self.__build_year = build_year
        
    def say_hi(self):
        if self.__name:
            print("Hi, I am " + self.__name)
        else:
            print("Hi, I am a robot without a name")
            
    def set_name(self, name):
        self.__name = name
        
    def get_name(self):
        return self.__name    

    def set_build_year(self, by):
        self.__build_year = by
        
    def get_build_year(self):
        return self.__build_year    
    
    def __repr__(self):
        return "Robot('" + self.__name + "', " +  str(self.__build_year) +  ")"

    def __str__(self):
        return "Name: " + self.__name + ", Build Year: " +  str(self.__build_year)

    
class A():
    
    def __init__(self):
        self.__priv = "I am private"
        self._prot = "I am protected"
        self.pub = "I am public"

        
class B():
	b = 'old'

  
if __name__ == "__main__":
    x = Robot("Marvin", 1979)
    y = Robot("Caliban", 1943)
    for rob in [x, y]:
        rob.say_hi()
        if rob.get_name() == "Caliban":
            rob.set_build_year(1993)
        print("I was built in the year " + str(rob.get_build_year()) + "!")

    
    aa = A()
    aa.pub += " and my value can be changed"
    print(x.pub)
    aa._prot += " and my value can be changed too"
    print(aa._prot)
    # x.__priv += 'whatever'    

    
    X = B()
    Y = B()
    print(X.b, Y.b)
    X.b = 'new'
    B.b = 'newer'
    print(X.b, Y.b, B.b)     
