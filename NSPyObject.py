
'''
Base Network Simulator Object 
All other classes will inherit this class.
We will add some common attributes to this class.

'''


class NSPyObject:

    def __init__(self):
        self._loggingEnabled = False  # We will use this attribute to enable message logging

    def enableLogging(self):
        self._loggingEnabled = True

    def disableLogging(self):
        self._loggingEnabled = False
