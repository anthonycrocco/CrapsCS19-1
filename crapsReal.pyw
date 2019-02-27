#!/usr/bin/env python

from die import *
import sys
import diceResources_rc
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication


class Craps(QMainWindow):
    """A game of Dice."""
    die1 = die2 = firstRoll = rollValue = currentBank = numberOfWins = numberOfLosses = None

    def __init__(self, parent=None):
        """Build a game with two dice."""

        super().__init__(parent)


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
        self.payouts = {2: 1, 3: 1, 4: 2, 5: 1.5, 6: 1.2, 7: 1, 8: 1.2, 9: 1.5, 10: 2, 11: 1, 12: 1}
        self.message = "Welcome to Craps!"
        uic.loadUi("Dice.ui", self)
        self.rollButton.clicked.connect(self.rollButtonClickedHandler)


    def __str__(self):
        return "FirstRoll: {0} RollValue: {1} Bank: {2} Wins: {3} Losses:{4}".format(self.firstRoll, self.rollValue, self.currentBank, self.numberOfWins, self.numberOfLosses)

    def getRollValue(self):
        return self.rollValue

    def getBetValue(self):
        return self.PlaceBet.value()

    def getFirstroll(self):
        return self.firstRoll

    def playRoll(self):
        pass



    def settleWin(self):
        self.numberOfWins += 1
        self.settleBet(self.firstRollValue, self.firstRoll, True, self.currentBet)
        self.message = "You Win!"
        print("win")

    def settleLoss(self):
        self.numberOfLosses += 1
        self.settleBet(self.rollValue, self.firstRoll, False, self.currentBet)
        self.message = "You Lost :("
        print("lost")

    def placeBet(self, valueToBet):
        self.currentBet = self.betValueUI.value()

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

    def updateUI(self):
        self.die1View.setPixmap(QtGui.QPixmap(":/" + str(self.die1.getValue())))
        self.die2View.setPixmap(QtGui.QPixmap(":/" + str(self.die2.getValue())))
        self.bankValueUI.setText(str(self.currentBank))
        self.winCounterUI.setText(str(self.numberOfWins))
        self.lossCounterUI.setText(str(self.numberOfLosses))
        self.displayUI.setText(self.message)

    # @QtCore.pyqtSignature("")				# Player asked for another roll of the dice.

    def rollButtonClickedHandler(self):
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
        print(self)
        self.updateUI()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    crapsApp = Craps()
    crapsApp.updateUI()
    crapsApp.show()
    sys.exit(app.exec_())
