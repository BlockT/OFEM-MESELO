from Episode import *
from window import *

class BruteForce():

    def __init__(self,events,minsup,delta,upperDelta,debug):
        self.minsup=minsup
        self.delta=delta
        self.upperDelta=upperDelta
        self.events=events
        self.debug=debug
        self.occurrences=set()
        self.sp={}

    def apply(self):

        for k in range(len(self.events)):
            if self.debug:
                print("Staring with event set"+str(k)+'+1...')
            self.brute(k)
            if self.debug:
                print('Occurences:')
                for ep in self.occurrences:
                    print(ep)
                print('spb=')
                print(self.sp)
        self.countFrequencies()
        if self.debug:
            print('Occurences:')
            for ep in self.occurrences:
                print(ep)
        print('spb-before=')
        print(self.sp)
        print("spb-after={}".format(self.sp))
        return self.frequentEpisode()

    def brute(self,k):
        print('!!!!!!!!!')
        newEventSet=self.events[k]
        tempOccurences=set()
        self.generateNew(Episode([],Window(k,k-1)),newEventSet,k,tempOccurences)
        for ep in self.occurrences.copy():
            if ep.window.start==k-self.upperDelta:
                 self.occurrences.remove(ep)
            if ep.window.start>=k-self.delta+1:
                 self.generateNew(ep,newEventSet,k,tempOccurences)
        self.occurrences=self.occurrences|tempOccurences
        self.filterOccurences()
        if self.debug:
            for ep in tempOccurences:
                print(ep)



    def generateNew(self,ep:Episode,newEventSet,timestamp,tempOccurences):
        for c in newEventSet:
            newlist=list(ep.events)
            newlist.append(c)
            generated=Episode(newlist,Window(ep.window.start,timestamp))

            tempOccurences.add(generated)
            if self.debug:
                print('Added:')
                print(generated)


    def filterOccurences(self):
        for toCheck in self.occurrences.copy():
            mustRemove=False
            for used in self.occurrences.copy():
                if toCheck.events==used.events and toCheck!=used and self.subsumedBy(used.window, toCheck.window):
                    mustRemove=True
                   #print('mustRemove')
                    if self.debug:
                       print('Filtered:'+str(toCheck)+'because of'+str(used))
            if mustRemove:
                self.occurrences.remove(toCheck)


    def countFrequencies(self):
        for ep in self.occurrences:
            newKey=str(ep.events)
            freq=self.sp.get(newKey)
            if freq==None or freq==0:
                self.sp.update({newKey:1})
            else:
                self.sp.update({newKey:freq+1})


    def subsumedBy(self,valid:Window,current:Window):
        return current.start<=valid.start and current.end>=valid.end

    def frequentEpisode(self):
        F=set()
        for get_L in self.sp.items():
            x,y=get_L
            if y>=self.minsup:
                F.add(x)
        return F



'''def summm(self,A,B):
        return A and B


occu=set([])
sp={}
occu.add((1,2))
print(occu,sp)
A=True
B=True
C=BruteForce(['A'],2,2,5,True)
print(C.summm(A,B))
'''
