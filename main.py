'''
How To Define a Class in Python? 

'''


class Node:
    pass


'''
We start with the class keyword to indicate that you are creating a class, 
then you add the name of the class

pass keyword:
    In Python we use the "pass" keyword (a statement) to indicate that nothing 
    happens—the function, class or loop is empty.

'''

'''
Classes create objects, and all objects contain characteristics called attributes.

Use the __init__() method to initialize (e.g., specify) an object’s initial attributes 
by giving them their default value.
'''


class Packet:
    # Initializer
    def __init__(self, dst, payload):
        self.destination = dst
        self.payload = payload


'''
 Example:
    Each packet has a destination attribute and a payload attribute.
    We use __init__(self,...) method to initialize object attribute.

    self in Packet example is an instance of the class.
    not all packets have the same destination or payload.

'''

'''
Class Attributes
    While instance attributes are specific to each object, 
    class attributes are the same for all instances- in our case all Packet objects
'''


class Node:
    # Class Attribute
    type = 'Node'
    # Initializer

    def __init__(self, ip, mac):
        self.ip = ip
        self.mac = mac


'''
while each Node has a unique ip and mac address, every node object will have a 
type attribute equal to 'Node'.
'''
