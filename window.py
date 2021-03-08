class Window():

    def __init__(self,start,end):
        self.start=start
        self.end=end

    def __str__(self):
        return '['+str(self.start)+','+str(self.end)+']'

#win=Window(1,2)
#print(win)