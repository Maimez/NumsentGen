#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


class NumberSentence:
    def __init__(self, min, max) -> None:
        self.a = random.randint(min, max)
        self.b = random.randint(min, max)
        self.op = None

    def __str__(self) -> str:
        if self.op is None:
            return 'the operator is not specified.'
        else:
            return f"{self.a} {self.op} {self.b} ="

    def __repr__(self) -> str:
        if self.op is None:
            return 'the operator is not specified.'
        else:
            source = f"{self.a} {self.op} {self.b}"
            return f"{self.a} {self.op} {self.b} = {eval(source)}"

    def __eq__(self, o: object) -> bool:
        if isinstance(o, NumberSentence):
            return str(self) == str(o)
        else:
            return False


class AdditionSentence(NumberSentence):
    def __init__(self, min=0, max=10) -> None:
        super().__init__(min=min, max=max)

        self.op = '+'
