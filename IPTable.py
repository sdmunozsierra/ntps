class IPTable:
     
    def __init__(self):
        self.status = False

    def toggleIPTableState(self):
        if (self.status == False):
            #add proper IPTable function to turn on IPTable
            self.status = True
        if (self.status == True):
            #add proper IPTable function to turn off IPTable
            self.status = False

    def getStatus(self):
        return self.status