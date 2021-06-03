#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .numbersentence import AdditionSentence
from .nsgenerator import generateNS


def main():
    nsGen = generateNS(AdditionSentence)

    for _ in range(10):
        ns = next(nsGen)
        print(ns, repr(ns))


if __name__ == '__main__':
    main()
