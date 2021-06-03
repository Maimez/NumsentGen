#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def generateNS(nsCls, duplicate=False):
    nslist = []
    ns = nsCls(max=5)
    while True:
        if duplicate:
            yield ns
        else:
            if ns not in nslist:
                nslist.append(ns)
                yield ns

        ns = nsCls(max=5)
