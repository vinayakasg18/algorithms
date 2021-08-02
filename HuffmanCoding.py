from typing import Any


""" Class to encode and decode the input string """


class HuffmanCoding:
    def recur(self, node, vi, val=''):
        """ Recur to add nodes with huffman codes """

        new_v = val + str(node.hufcode)

        if(node.left):
            self.recur(node.left, vi, new_v)
        if (node.right):
            self.recur(node.right, vi, new_v)
        if not node.left and not node.right:
            vi[node.sym] = new_v
        return vi

    def build(self, text: str) -> Any:
        """ Function to build a huffman tree """
        
        d = {}
        for ch in text:
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1
        nodes = []
        for i in d:
            nodes.append(Node(d[i], i))
        while len(nodes) > 1:
            nodes = sorted(nodes, key=lambda x: x.freq)
            l = nodes[0]
            r = nodes[1]

            l.hufcode = '0'
            r.hufcode = '1'

            new_node = Node(l.freq+r.freq, l.sym+r.sym, l, r)
            nodes.remove(l)
            nodes.remove(r)
            nodes.append(new_node)
        y = {}
        w = self.recur(nodes[0], y)
        encoded = self.encode(w, text)
        print(encoded)
        decoded = self.decode(w, encoded)
        print(decoded)

        return w

    def encode(self, Dic: Any, text: str) -> str:
        """ Function to encode the input text using a dictionary(hufman tree) """

        s = ''
        for i in text:
            s += Dic[i]
        return s

    def decode(self, Dic: Any, text: str) -> str:
        """ Functiont to decode the code """

        d = {}
        for k, v in Dic.items():
            d[v] = k
        i = 1
        final = ''
        while(len(text) != 0):
            if text[:i] in d.keys():
                final += d[text[:i]]
                text = text[i:]
                i = 1
            else:
                i += 1
        return final


""" Class to generate the Node/Tree """


class Node:
    def __init__(self, freq, sym, left=None, right=None):
        self.freq = freq
        self.sym = sym
        self.left = left
        self.right = right
        self.hufcode = ''


print(HuffmanCoding().build("AABCCDDDD"))
