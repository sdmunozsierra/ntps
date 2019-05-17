"""
Cook class will provide its information to the classes that need it.
"""
import os
import fnmatch
import subprocess
from pyutils import check_file_exists, extract_hook_name
# from Hooks import *
# import Hooks
from Hooks import DNSsport


class TestHook:

    def __init__(self, name, description, status, hookOrder, path):
        self.path = path
        self.name = name
        self.description = description
        self.status = status  # Boolean
        self.hookOrder = hookOrder
        self.real_name = extract_hook_name(self.path)

    def run_hook(self, a_hook, packet):
        print("Will try to run hook_real name: {}".format(a_hook.real_name))
        if a_hook.real_name == "DNSsport":
            print("Running DNSsport")
            # hook = DNSsport()
            r_hook = DNSsport.DNSsport()
            return r_hook.changeSport(packet)
        return None


    # def run(self, hook, packet):
    #     """Run a hook
    #     :param hook: filepath containing hook.
    #     :param packet: packet to be run by the hook.
    #     """
    #     self.status = True
    #     if not check_file_exists(hook):
    #         return  # No hook selected or valid (maybe raise exception)
    #
    #     # run without shell
    #     # subprocess.run(["python3", "{}".format(hook), packet], capture_output=True)
    #     process = subprocess.Popen(["python3", "{}".format(hook), packet], stdout=subprocess.PIPE)
    #     out, err = process.communicate()
    #     # print(out)
    #     return out
    #

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
