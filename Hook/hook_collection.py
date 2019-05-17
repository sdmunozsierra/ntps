"""
HookCollection class will provide its information to the classes that need it.
"""


class hookCollection:

    def __init__(self, name, num, status, description):
        self.name = name
        self.number = num
        self.status = status
        self.description = description

    def getHookCollectionName(self):
        return self.name

    def getHookCollecitonStatus(self):
        return self.status

    def getHookCollecitonDescription(self):
        return self.description

    def getHookCollectionSequence(self):
        return self.number

    def addHookCollection(self):
        return self.name

    def getHookCollectioninfo(self, hookCollection):
        #For loop go through all the list
        #Call hook.getinfo on each
        pass
