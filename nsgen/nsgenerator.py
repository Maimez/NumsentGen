#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from reportlab.lib import colors


class NSGenerator:
    def __init__(self, nscls, rows=5, cols=4, min=0, max=10) -> None:
        self.rows = rows
        self.cols = cols
        self.nscls = nscls
        self.min = min
        self.max = max

    def gen(self):
        nsgen = _generateNS(self.nscls, self.min,
                            self.max, self.rows*self.cols)
        nsList = []

        for _ in range(self.rows):
            ns = []
            for _ in range(self.cols):
                ns.append(next(nsgen))
            nsList.append(ns)

        return nsList


def _generateNS(nsCls, min, max, total, duplicate=False):
    nslist = []
    if not duplicate and (max-min+1)**2 < total:
        duplicate = True
    ns = nsCls(min, max)
    count = 0
    while count < total:
        if duplicate:
            count += 1
            yield ns
        else:
            if ns not in nslist:
                nslist.append(ns)
                count += 1
                yield ns
        ns = nsCls(min, max)
