import os
import fnmatch
class hook:
    #lists of hooks
    global hooks
    global path
    path = "usr/bin/ntps/hooks/"

    def __init__(self, name, description, status, hookOrder):
        self.name = name
        self.description = description
        self.status = status
        self.hookOrder = hookOrder
    def addhook(self, hook):
        try:
            hooks.insert(hook)
            #Create a file with it's path
            path =+hook.name
            if not os.path.exists(path):
                os.mkdir(path)
            else:
                print("File already exists with same name")
        except:
            print("Unable to create new object, check parameters")
    def gethookinfo(self, hook):
        try:
            hookinfo = [hook.name, hook.description, hook.status, hook.hookOrder]
            return hookinfo
        except:
            print("Failed to find this hook's info")
    def searchhook(self, hookname):
       try:
            for file in os.listdir('.'):
                if fnmatch.fnmatch(file, hookname):
                    return True
            return False
       except:
           print("Unable to traverse the directory")
    def deletehook(self, hook):
        try:
            check = False
            #Loop through all of our list and remove it from our lists
            for i in hook.hooks:
                if hook.name == hook.hooks[i].name:
                    hook.hooks.remove(i)
                    check = True

            if check is False:
                print("Was not able to locate requested hook name")

        except:
            print("Was unable to delete hook")
    def run(self, hook):
        self.status = True
        #I think
        #Stackoverflow said so...
        os.system(hook.name)
        #Executes teh specified python code
        #Also assumes that the script name includes the .py
        exec(hook.name)




