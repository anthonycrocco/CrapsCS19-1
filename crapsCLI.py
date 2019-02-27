#!/usr/bin/env python
__author__ = "Anthony Crocco"

from die import *


class CrapsCLI(object):
    def __init__(self):
        self.die1 = Die()
        self.die2 = Die()
        self.currentBet = 0
        self.rollValue = 0
        self.beginningBank = 2000
        self.currentBank = self.beginningBank
        self.firstRoll = True
        self.firstRollValue = 0
        self.numberOfWins = 0
        self.numberOfLosses = 0
        self.payouts = {4:2, 5:1.5, 6:1.2, 8:1.2, 9:1.5, 10:2}

    def __str__(self):
        return "FirstRoll: {0} RollValue: {1} Bank: {2} Wins: {3} Losses:{4}".format(self.firstRoll, self.rollValue, self.currentBank, self.numberOfWins, self.numberOfLosses)

    def getRollValue(self):
        return self.rollValue

    def getBetValue(self):
        return self.PlaceBet.value()

    def getFirstroll(self):
        return self.firstRoll

    def playRoll(self):
        self.placeBet(50)
        self.rollValue = self.die1.roll() + self.die2.roll()
        print("Rolled a {0}".format(self.getRollValue()))
        if self.firstRoll:
            if self.rollValue in (7, 11):
                self.settleWin()
            elif self.rollValue in (2, 3, 12):
                self.settleLoss()
            else:
                self.firstRoll = False
                self.firstRollValue = self.rollValue
        else:  # play second roll
            if self.rollValue == self.firstRollValue:
                self.settleWin()
            else:
                self.settleLoss()
            self.firstRoll = True
        return self.firstRoll

    def settleWin(self):
        self.numberOfWins += 1
        self.settleBet(self.firstRollValue, self.firstRoll, True, self.currentBet)
        print("win")

    def settleLoss(self):
        self.numberOfLosses += 1
        self.settleBet(False, self.rollValue, self.firstRoll, self.currentBet)
        print("lost")

    def placeBet(self, valueToBet):
        self.currentBet = 50

    def settleBet(self, firstRollValue, firstRoll, wonGame, betValue):
        if firstRoll:
            if wonGame:
                self.currentBank += betValue
            else:
                self.currentBank -= betValue
        else:
            if wonGame:
                self.currentBank += betValue * self.payouts[firstRollValue]
            else:
                self.currentBank -= betValue * self.payouts[firstRollValue]

    def quitGame(self):
        pass


gameObject = CrapsCLI()
for number in range(0, 1):
    if not gameObject.playRoll():
        gameObject.playRoll()
        print(gameObject)

