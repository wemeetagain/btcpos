
#For debugging without LCD - just write to stdout.
class stdout:
    def __init__(self):
        self.tl = ""
        self.bl = ""

    def clear(self):
        pass

    def setTopLine(self, text):
        self.tl = text

    def setBottomLine(self,text):
        self.bl = text

    def printLCD(self):
        print self.tl + "\n" + self.bl

    def printTopLine(self):
        print self.tl + "\n"

    def printBottomLine(self):
        print self.bl + "\n"


