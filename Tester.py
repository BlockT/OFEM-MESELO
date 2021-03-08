from window import *
from Trie import *
from Episode import *
from Generator import *
from BruteForce import *
from Meselo import *
import time
class Tester():
    minSup=2
    delta=5
    upperDelta=20
    size=20
    nEvents=6
    debug=False


    gen=Generator(42)

    eventSeq=gen.generate(size,nEvents)
    print('Event sequence:')
    print(eventSeq)
    
    bf=BruteForce(eventSeq,minSup,delta,upperDelta,debug)
    t1=time.time()
    F1=bf.apply()
    t2=time.time()
    print('F1')
    print(F1)

    m=Meselo(eventSeq,minSup,delta,upperDelta,debug)
    t3=time.time()
    F2=m.apply()
    t4=time.time()
    print('F2')
    print(F2)
    print("Comparison:"+str(F1==F2))

    btime=(t2-t1)
    mtime=(t4-t3)
    print('btime:'+str(btime)+"VS"+'mtime'+str(mtime))

    print('Other small custom test...')
    customSeq=gen.generateCustom()
    print('CustomSequence:')
    print(customSeq)
    bf2=BruteForce(customSeq,1,3,3,debug)
    m2=Meselo(customSeq,1,3,3,debug)
    t5 = time.time()
    F3=bf2.apply()
    t6 = time.time()
    print('F3')
    print(F3)
    t7 = time.time()
    F4=m2.apply()
    t8 = time.time()
    print('F4')
    print(F4)
    btime2 = (t6 - t5)
    mtime2 = (t8 - t7)
    print('btime:' + str(btime2) + "VS" + 'mtime' + str(mtime2))
    print('Comparison:'+str(F3==F4))

#    print(eventSeq)
    print('end........')



'''
win=Window(1,2)
trie=Trie.Trie('A',2)
episode=Episode.Episode(['A','B'],Window(2,3))
print(win)
print(trie)
print(episode)
'''
