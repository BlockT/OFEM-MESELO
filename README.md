# OFEM-MESELO
OFEM(Online Frequent Episode Mining)旨在识别频率大于用户指定阈值的所有频繁事件集。MESELO(Mining frEquent Serial Episode via Last Occurrence)是一种新的在线频繁事件集挖掘算法。
因为暴力挖掘方法在当前时间窗口内对事件序列连续执行批处理，将导致大量重复运算，时间复杂度高；所以开发MESELO算法采用Trie数据结构，简化对事件集进行遍历操作的时间复杂度，提出高效算法。
