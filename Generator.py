import random

class Generator():

    def __init__(self,seed):
        random.seed(seed)

    def generate(self,size,max):
        events=[]
        for i in range(0,size):
            nEvents=random.randint(0,max)
            event=[]
            for j in range(0,nEvents+1):
                letter = chr(ord('A')+random.randint(0, 25))  #随机生成字母A-Z
                if letter not in event:
                    event.append(letter)
            events.append(event)
        return events

    def generateCustom(self):
        events=[['A'],['B'],['C'],['D','E'],['F']]
        return events
'''
a=['1','2','3']
b=['1','2','3']
print(a==b)
调试随机数和数组功能
events=['1',1,[1,2]]
event=['A']
letter = chr(random.randint(65, 91))
if letter not in event:
    event.append(letter)
events.append(event)
print(event)
print(events)
'''
