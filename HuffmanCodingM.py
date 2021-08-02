from typing import Any
from heapq import *
from itertools import groupby

class HuffmanCoding:
    left_child = None
    right_child = None
    item = None
    weight = None

    def __init__(self, i, w):
        self.item = i
        self.weight = w

    def setChildren(self, ln, rn):
        self.left_child = ln
        self.right_child = rn

    def __repr__(self):
        return "%s - %s -- %s _ %s" % (self.item, self.weight, self.left_child, self.right_child)

    def __cmp__(self, a):
        return cmp(self.weight, a.weight)

    def build(self, text : str) -> Any:
        d = {}
        node = 0

        for c in text:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        
        # sorted_dict = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}

        sorted_dict = [Node(a, len(list(b))) for a, b in groupby(sorted(input))]
        
        # for key, value in sorted_dict.items():
        #     if node > value:
        #         node = value
        #     else:
        #         node = 

        heapify(sorted_dict)

        while len(sorted_dict) > 1:
            l = heappop(sorted_dict)
            r = heappop(sorted_dict)
            n = Node(None, r.weight+l.weight)
            n.setChildren(l,r)
            heappush(sorted_dict, n)

    
    def encode(self, Dic : Any, text : str) -> str:
        codes = {}

    def codeIt(s, node):
        if node.item:
            if not s:
                codes[node.item] = "0"
            else:
                codes[node.item] = s
        else:
            codeIt(s+"0", node.left)
            codeIt(s+"1", node.right)
	

codeIt("",itemqueue[0])

    def decode(self, Dic : Any, text : str) -> str:
        pass

print(HuffmanCoding().build("AAAB"))