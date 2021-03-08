class Trie():

    def __init__(self,event,time):
        self.event=event
        self.time=time
        self.children=[]
        self.isLO=True

    def __str__(self):
        return 'event('+self.event+'),time('+str(self.time)+'),isLO('+str(self.isLO)+'),children('+','.join(str(self.children))+')'