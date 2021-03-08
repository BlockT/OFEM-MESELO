from window import Window

class Episode():

    def __init__(self,events:list,window:Window):
        self.events=events
        self.window=window

    def __hash__(self):
        return hash(str(self.events))

    def __eq__(self, other):
        return self.__dict__==other.__dict__



    def __str__(self):
        return str(self.events)+' '+str(self.window)