"""
Field class will provide its information to the classes that need it.
"""


class Field:

    def __init__(self, name, value, mask, display_format, selected):
        self.name = name
        self.value = value
        self.mask = mask
        self.display_format = display_format
        self.selected = selected

    def setName(self, name):
        self.name = name

    def setValue(self, value):
        self.value = value

    def setMask(self, mask):
        self.mask = mask

    def setDisplayFormat(self, display_format):
        self.display_format = display_format

    def setSelected(self, selected):
        self.selected = selected
