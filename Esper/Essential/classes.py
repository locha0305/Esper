#imports
import parser


#this is a 'Class' class
class Class():
    def __init__(self):
        self.attributes = {}
    def add_attr(self, name, attr):
        self.attributes[name] = attr
    def show_attr(self, name):
        return self.attributes[name]



#this is a 'Function' class
class Function():
    def __init__(self):
        self.code = []
        self.attributes = {} #when executed
        self.type = "FUNCTION" #also can be 'builtin' which uses python code to execute


