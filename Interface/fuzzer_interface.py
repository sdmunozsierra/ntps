class fuzzerInterface:
    
    def __init__(self):
        self.soemthing = 0

    def fuzzData(self, data):
        pass

    def saveFuzzed(self, packets):
        pass

#afl-fuzz -i [input_directory] -o [output_directory] ./[executable_to_fuzz] @@