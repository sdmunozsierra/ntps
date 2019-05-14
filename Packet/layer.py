"""
Layer class will provide its information to the classes that need it.
"""


class Layer:

    ########## TODO: field array
    
    
    def __init__(self, fields ,field_name, show_name, position, value):
        self.fields = list()
        self.field_name = field_name
        self.show_name = show_name
        self.size = None
        self.position = position
        self.show = False
        self.value = value

    def getLayers(self):
        return self.fields
