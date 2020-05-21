'''
Singleton
'''


'''
Method __new__ will take class reference as the first argument followed by arguments which are 
passed to constructor(Arguments passed to call of class to create instance). 
Method __new__ is responsible to create instance, so you can use this method to customize object creation.
Typically method __new__ will return the created instance object reference. 
Method __init__ will be called once __new__ method completed execution.
'''


class OnlyOne:

    # class attribute
    _instance = None

    def __new__(cls, name):
        if cls._instance is None:  # this is the first time we create an object of this type
            cls._instance = super(OnlyOne, cls).__new__(cls)

        return cls._instance

    def __init__(self, name):
        self.name = name


o1 = OnlyOne("node1")
print(o1)
print(o1.name)
o2 = OnlyOne("node2")
print(o2)
print(o2.name)
