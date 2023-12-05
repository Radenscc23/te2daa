__author__ = "Andrea Rubbi"
import time


def set_cover(universe, subsets,costs):
    cost=0
    elements = set(e for s in subsets for e in s)
    if elements != universe:
        return None
    covered = set()
    cover = []
    while covered != elements:
        subset = max(subsets, key=lambda s: len(s - covered)/costs[subsets.index(s)])
        cover.append(subset)
        cost+=costs[subsets.index(subset)]
        covered |= subset
 
    return cover, cost
 
def main(a,b,c,x=time.time()):
    m= a
    universe = set(range(1, m+1))
    sub = b  
    
    subsets = [set(x) for x in sub]
    costs =  c 
    cover = set_cover(universe, subsets,costs)
    print('covering sets= ',cover[0],'\n',
          'cost= ',cover[1],'$')
    print('time: ',time.time()-x)