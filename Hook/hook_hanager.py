import os
from Hook.hook import hook
class hookManager:
    """
    Hooks will be created here
    """
    def __init__(self):
        self.hooks = []
        self.hookColleciton = []

    #File directory
    #locaiton of files
    path = "Hooks/"
    if not os.path.exists(path):
        os.mkdir(path)


    """
    @requires hook to be file, description to be string, stat to be the status, seq to be a int
    """

    def addHook(self, hook):
        self.hooks.append(hook)
        
    def addhook(self, hookname, description, stat, seq, path):
        
        newhook = hook(hookname, description, stat, seq, path)
        print("Hook object name is ",newhook.name)
        #hook.addhook(hookname, description, stat, seq)
        self.hooks.append(newhook)
        fname =f"Hooks/{newhook.name}.py"
        print(fname)
        if not os.path.exists("Hooks/"):
            print("creating dir")
            os.mkdir("Hooks")
        else:
            print("Dir already exists with same name")
        with open(path) as f:
            with open(fname, "w+") as f1:
                for line in f:
                    f1.write(line)
        

    def deletehook(self, hook):
        try:
            hook.deletehook(hook)
        except:
            print("Unable to search this hook")

    def searchhook(self, hookname):
        for hook in self.hooks:
            if hook.name == hookname:
                return hook

        return None

    def hookinfo(self, hook):
        pass

    def getHook(self, hookname):
        pass
    
    def runhook(self, hook):
        try:
            hook.run()
        # TODO Create an exception for run hook
        except:
            print("Unable to run hook")

    def addHookColleciton(self, hook_collection):
        print("AddHookCollection")
        return

    def deleteHookCollection(self, hook_collection):
        print("DeleteHookCollection")
        return

    def hookCollectionInfo(self, hook_collection):
        print("InfoHookCollection")
        return
