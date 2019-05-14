import os
import hook
class hookManager:
"""
Hooks will be created here
"""
hooks = []
hookColleciton = []

#File directory
#locaiton of files
path = "~/usr/bin/ntps/hooks/"
if not os.path.exists(path):
    os.mkdir(path)


"""
@requires hook to be file, description to be string, stat to be the status, seq to be a int
"""
def addhook(self, hookname, description, stat, seq):
    try:
        newhook = hook(hookname, description, stat, seq)
        #hook.addhook(hookname, description, stat, seq)
        hooks.add(hook)
        path =+hook.name
        if not os.path.exists(path):
            os.mkdir(path)
        else:
            print("File already exists with same name")

    except:
        print("Unable to enter add hook method")
def deletehook(self, hook):
    try:
        hook.deletehook(hook)
    except:
        print("Unable to search this hook")
def searchhook(self, hookname):
    try:
        hook.search(hookname)
    except:
        print("Unable to search this hook")
def hookinfo(self, hookname):
    try:
        hook.info(hookname)
    except:
        print("Unable to return hook info")
def runhook(self, hook):
    try:
        hook.run()
    except:
        print("Unable to run hook")


def addHookColleciton(self, hookCollection):
    return FAILURE
def deleteHookCollection(self, hookCollection):
    return FAILURE
def hookCollectionInfo(self, hookCollection):
    return FAILURE
