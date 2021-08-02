from heapq import heappush, heappop, heapify
from typing import Any


class HuffmanCoding:

    def build(self, text: str) -> Any:
        d = {}
        for c in text:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1

        heap = [[value, [key, ""]] for key, value in d.items()]

        heapify(heap)
        while len(heap) > 1:
            low = heappop(heap)
            high = heappop(heap)
            for chp in low[1:]:
                chp[1] = '0' + chp[1]
            for chp in high[1:]:
                chp[1] = '1' + chp[1]
            heappush(heap, [low[0] + high[0]] + low[1:] + high[1:])

        sorted_dict = sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

        for i in range(len(sorted_dict)):
            d[sorted_dict[i][0]] = sorted_dict[i][1]

        d = dict(sorted(d.items(), key=lambda item: item[1]))
        enc = self.encode(d, text)
        dec = self.decode(d, enc)
        return d

    def encode(self, Dic: Any, text: str) -> str:

        enc = ""
        for i in text:
            enc = enc + Dic[i]

        return (enc)

    def decode(self, Dic: Any, text: str) -> str:
        d = dict([(value, key) for key, value in Dic.items()])
        dec = ""
        t_dec = ""

        enc_chars = []

        for key, value in d.items():
            enc_chars.append(key)

        for i in text:
            t_dec += i
            if t_dec in enc_chars:
                dec += d[t_dec]
                t_dec = ""
            else:
                continue

        return (dec)
