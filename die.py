#!/usr/bin/env python
from random import randint

__author__ = "Anthony Crocco"
class Die(object):

    def __init__(self, beginningSides = 6, beginningStartingValue = 1, beginningColor = "Bone"):
        self.value = 0
        self.numberOfSides = beginningSides
        self.startingValue = beginningStartingValue
        self.color = beginningColor

    def __str__(self):
        return "{0}".format(self.getValue())
    def getValue(self):
        return self.value
    def setValue(self, newValue = 0):
        self.value = newValue
    def roll(self):
        self.value = randint(1, self.numberOfSides)
        return self.value