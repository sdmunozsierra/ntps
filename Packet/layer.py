"""
Layer class will provide its information to the classes that need it.
"""


class Layer:

    ########## TODO: field array

    def __init__(self, fields, field_name, show_name, position, value):
        self.fields = self.init_fields(fields)
        self.field_name = field_name
        self.show_name = show_name
        self.size = None
        self.position = position
        self.show = False
        self.value = value

    def init_fields(self, fields):
        field_list = list()
        for field in fields:
            field_list.append(field)
        return field_list

    def getLayers(self):
        return self.fields
