__author__ = 'mahesh.nayak'

import sys

l = lambda a: a > 0
def cutSticks(lengths):
    lengths = filter(l, lengths)
    while len(lengths) > 0:
        print len(lengths)
        min_val = min(lengths)
        lengths = [x - min_val for x in lengths]
        lengths = filter(l, lengths)


_lengths_cnt = int(raw_input())
_lengths_i = 0
_lengths = []
while _lengths_i < _lengths_cnt:
    _lengths_item = int(raw_input());
    _lengths.append(_lengths_item)
    _lengths_i += 1

cutSticks(_lengths)

