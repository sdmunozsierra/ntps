
import os
from pyutils import create_packet
from Hook.hook import Hook


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
    def addhook(self, hookname, description, stat, seq, path):
        newhook = Hook(hookname, description, stat, seq, path)
        print("Hook object name is ", newhook.name)
        self.hooks.append(newhook)
        fname = f"Hooks/{newhook.name}.py"
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
        """Removes a hook from the list."""
        if hook in self.hooks:
            print(f"Removing hook: {hook.name}")
            self.hooks.remove(hook)

    def searchhook(self, hookname):
        for hook in self.hooks:
            if hook.name == hookname:
                return hook
        return None

    def hookinfo(self, hook):
        # for hook in self.hooks:
        #     hook.get_hook_info(hook)
        # pass
        if hook in self.hooks:
            hook.get_hook_info(hook.name)

    def getHook(self, hookname):
        for hook in self.hooks:
            if hook.name == hookname:
                return hook

    def runhooks(self, packet):
        """Runs all hooks in the hooks list."""
        for hook in self.hooks:
            hook.run_hook(hook, packet)

    def createHookCollection(self):
        pass

    def addHookColleciton(self, hook_collection):
        print("AddHookCollection")
        return

    def deleteHookCollection(self, hook_collection):
        print("DeleteHookCollection")
        return

    def hookCollectionInfo(self, hook_collection):
        print("InfoHookCollection")
        return
