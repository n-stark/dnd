import dnd
import random
import numpy as np

class campaign(object):
    def __init__():
        self.adventurors = [] #list of character objects
        self.npcs = []#list of NPC objects

        self.action = 1
        self.bonusAction = 1
        self.Reaction = 1

    def loadPC(self, PC):
        self.adventurors.append(PC)

    def updateCharacters(self):

    def addNPCs(self, npc):
        self.npcs.append(npc)

    def removeNPCs(self, name):
        self.npcs.remove(npc)

    def printCharacters(self):

    def writeStory(self):

class combat(object):
        """
        rolls initative
        keeps turn order, actions, and rounds
        """
    def __init__():
        self.combatants = []
        self.inititiveRoll= [] #initialive roll  for each combatant

        self.turnOrder = []
        self.round = 1
        self.currentTurn = turnOrder[0].name

        self.action = 1
        self.bonusAction = 1
        self.Reaction = 1

    def addCombatant(self,combatant):
        self.combatant.append(combatant)

    def removeCombatant(self,combatant):
        self.combatant.remove(combatant)

    def rollInitive(self):

    def endTurn(self):
        self.currentTurn = self.turnOrder[+1].name

    def newRound(self):
        self.round += 1

    def weaponattack(self, ch1, ch2):

    def rangedspellattack(ch1, ch2):

    def castspell(c1, spell, ch2):
