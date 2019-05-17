"""
Cook class will provide its information to the classes that need it.
"""
import os
import fnmatch
from Tests.Test_Hooks import DNSsport


class TestHook:
    def __init__(self, name, description, status):
        self.path = None
        self.name = name
        self.description = description
        self.status = status  # Boolean

    def run(self, hook, packet):
        """Run a hook
        :param hook: filepath containing hook.
        :param packet: packet to be run by the hook.
        """
        self.status = True

        # os.system(hook.name)
        #Executes teh specified python code
        #Also assumes that the script name includes the .py
        # exec(hook.name)
        subprocess.run("exit 1", shell=True, check=True)


class hook:

    global hooks
    global path

    def __init__(self, name, description, status, hookOrder, path):
        self.path = path
        self.name = name
        self.description = description
        self.status = status  # Boolean
        self.hookOrder = hookOrder

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
        # os.system(hook.name)
        #Executes teh specified python code
        #Also assumes that the script name includes the .py
        # exec(hook.name)
        subprocess.run("exit 1", shell=True, check=True)
