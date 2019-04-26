from subprocess import call
class IPTable:
     
    def __init__(self):
        self.status = False

    def toggleIPTableState(self):
        if (self.status == False):
            #add proper IPTable function to turn on IPTable this could be the wrong command still not sure
            call('systemctl enable ufw', shell = True)
            self.status = True
        if (self.status == True):
            #add proper IPTable function to turn off IPTable this could be the wrong command still not sure
            call('systemctl disable ufw', shell = True)
            self.status = False

    def getStatus(self):
        return self.status