import time
from Trie import *
from Episode import *
from window import *
import sys
class Meselo():

    def __init__(self,events,minsup,delta,upperdelta,debug):
        self.minsup=minsup
        self.delta=delta
        self.upperdelta=upperdelta
        self.events=events
        self.debug=debug

        self.M_ex=[]
        self.M_in=[]
        self.C=set()
        self.F=set()
        self.sp={}

    def apply(self):
        i=-1
        for newEventSet in self.events:
            if self.debug:
                print("Iteration k = "+ str(i) +"...")
            self.meselo(newEventSet,i)
            if self.debug:
                print("F = ")
                print(self.F)
                print("C = ")
                print(self.C)
                print("sp = ")
                print(self.sp )
            i+=1
        print("sp = ")
        print(self.sp)
        return self.F

    def buildTrie(self,newEventSet,k):
        root=Trie('0',k+1)
        for c in newEventSet:
            node=Trie(c,k+1)
            root.children.append(node)
        return root

    def updateTries(self,M_in,newEventSet,k):
        Q=set()
        for c in newEventSet:
            list=[]
            list.append(c)
            Q.add(Episode(list,Window(k+1,k+1)))
        i=k
        if self.debug:
            print("Q after adding 1-episodes:"+ str(Q))
        while i>=k-self.delta+2 and i>=0:
            if self.debug:
                print("M_in:"+str(M_in))
            t=self.M_in[len(self.M_in)-(k-i)-2]
            if self.debug:
                print("t grabbed from M_in:")
                print(t)
            self.travel(t,[],t.time,newEventSet,i,k,Q)
            i-=1
        return Q

    def travel(self,t,currentPath,startTime,newEventSet,i,k,Q):
        path=currentPath.copy()
        children=t.children.copy()
        if t.event!='0':
            path.append(t.event)
            if t.isLO:
                alpha=Episode(path,Window(startTime,t.time))
                if self.debug:
                    print("alpha :")
                    print(alpha)
                self.visit(t,alpha,newEventSet,i,k,Q)
        for child in children:
            self.travel(child,path,startTime,newEventSet,i,k,Q)

    def visit(self,p,alpha,newEventSet,i,k,Q):
        for e in newEventSet:
            comparison=False
            for child in p.children:
                if child.event==e:
                    comparison=True
            if comparison:
                if self.debug:
                    print('Already have')
            else:
                q=Trie(e,k+1)
                p.children.append(q)
                if self.debug:
                    print("New Trie:")
                    print(p)
                    print("alpha.events:"+str(alpha.events))
                qAlphaPath=alpha.events.copy()
                if self.debug:
                    print("qAlphaPath:"+str(qAlphaPath))
                qAlphaPath.append(e)
                qAlpha=Episode(qAlphaPath,Window(i,k+1))
                Q.add(qAlpha)
                if self.debug:
                    print("New Q:")
                    for ep in Q:
                        print(Q)
        contained=False
        for ep in Q:
            if str(ep.events)==str(alpha.events):
                contained=True
        if contained:
            p.isLO=False
        if self.debug:
            print("P:")
            print(p)

    def outputF(self,Q,k,upperDelta,minSup):
        if k-upperDelta+1>=0:
            loaded=self.M_ex[k - upperDelta + 1]
            if self.debug:
                print("M_ex:")
                print(self.M_ex)
                index=k-upperDelta+1
                print("M_ex.size()="+str(len(self.M_ex))+",index of loaded="+str(index))
                print("Loaded from M_ex:")
                print(loaded)
            if self.debug:
                print("sp-before:")
                print(self.sp)
            self.travel2(loaded,[],loaded.time)

        for alpha in Q:
            newkey=str(alpha.events)
            if self.debug:
                print("new_alpha.events:"+str(alpha.events))
            freq=self.sp.get(newkey)
            if freq==None:
                self.sp.update({newkey:1})
            else:
                self.sp.update({newkey:freq+1})

        if self.debug:
            print("sp-after:"+str(self.sp))

        self.F=set()
        self.C=set()
        for get_L in self.sp.items():
            x,y=get_L
            if y>=self.minsup:
                self.F.add(x)
            else:
                self.C.add(x)
        return self.F

    def travel2(self,t,currentPath,startTime):
        path=currentPath.copy()
        if t.event!='0':
            path.append(t.event)
            alpha=Episode(path,Window(startTime,t.time))
            newkey=str(alpha.events)
            freq=self.sp.get(newkey)
            if self.debug:
                print("alpha.events:"+str(alpha.events))
            if freq==None or freq==0:
                if self.debug:
                    print("Eipsode not found in map:"+alpha)
            elif freq==1:
                del(self.sp[newkey])
            else:
                self.sp.update({newkey:freq-1})
        for child in t.children:
            self.travel2(child,path,startTime)

    def meselo(self,newEventSet,k):
        print('!!!!!!!!!')
        if self.debug:
            print("New event set:"+str(newEventSet))
        newTrie=self.buildTrie(newEventSet,k)
        if self.debug:
            print("newTrie:"+str(newTrie))
            print("M_in:"+str(self.M_in))
        self.M_in.append(newTrie)
        if self.debug:
            print("M_in after adding newTrie:"+str(self.M_in))
        Q=self.updateTries(self.M_in,newEventSet,k)
        if self.debug:
            print("Q after 'updateTries':"+str(Q))

        if(len(self.M_in)==self.delta):
            #print("*******M_in[0]:")
           # print(self.M_in[0])
           # print(self.M_in[0].children)
            toSwitch=self.M_in[0]
            self.M_in.remove(self.M_in[0])
           # print("***TOSEITCH:")
           # print(toSwitch)
            self.M_ex.append(toSwitch)
        if self.debug:
            print("Last M_in:"+str(self.M_in))
            print("Last M_in size:"+str(len(self.M_in)))
            print("Last M_ex:"+str(self.M_ex))
            print("Last M_ex size:" + str(len(self.M_ex)))
        self.F=self.outputF(Q,k,self.upperdelta,self.minsup)





'''i='boy'
a=set('boy')
a.add('python')
a.add(i)
a.add(Trie('0',1))
a.add(Episode('A',Window(0,1)))

print(a)

c=[1,2,3]
c.remove(c[0])
print(c)'''
