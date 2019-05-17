
import os
from pyutils import create_packet
from Hook.hook import hook, TestHook


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

        # newhook = hook(hookname, description, stat, seq, path)
        newhook = TestHook(hookname, description, stat, seq, path)
        print("Hook object name is ", newhook.name)
        #hook.addhook(hookname, description, stat, seq)
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

    def runhook(self, hook, packet):
        # TEST RUN HOOK
        # pkt = 'E\x00\x00\x14\x00\x01\x00\x00@\x00|\xe7\x7f\x00\x00\x01\x7f\x00\x00\x01'
        # pkt = create_packet(pkt)
        # TODO check if packet is already a packet
        hook.run_hook(hook, packet)
        print("HOOK RUN")

    def addHookColleciton(self, hook_collection):
        print("AddHookCollection")
        return

    def deleteHookCollection(self, hook_collection):
        print("DeleteHookCollection")
        return

    def hookCollectionInfo(self, hook_collection):
        print("InfoHookCollection")
        return