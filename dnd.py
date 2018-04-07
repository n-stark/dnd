import numpy as np
import copy as copy
import random

class character(object):
    def __init__(self):
        self.name = str()
        self.race = str()
        self.movement = 30
        self.class = []
        self.level = 0
        self.proficiencyBonus = 0

        self.strength = 0
        self.strMod = (self.strength-10)/2
        self.dexterty = 0
        self.dexMod = (self.dexterty-10)/2
        self.constitution = 0
        self.conMod = (self.constitution-10)/2
        self.intelligence = 0
        self.intMod = (self.intelligence-10)/2
        self.wisdom = 0
        self.wisMod = (self.wisdom-10)/2
        self.charisma = 0
        self.chaMod = (self.charisma-10)/2

        self.armorClass = 0
        self.hitpointsMax = 0
        self.currentHitpoints = 0
        self.passiveperception = 1.
        self.initialize = 1.

        self.armor = []
        self.weapons = [] #list of weapon objects
        self.items = [] #list of item objects
        self.currency = [] #gold silver than copper

        self.carryMax = 1
        self.weight = 1.

        self.spellslots = [] #first element is number of 1st level slots
        self.spellsknow = [] #list of spell objects

    #Change stats
    def levelup(self):
        self.level += 1

    def damage(self, dmg):
        self.currenthitpoints += dmg

    def heal(self, hp):
        self.currenthitpoints += hp

    def abilityscoreimprovement(self, ability, number):
        self.ability += number

    def learnspell(self, spell):
        self.spellsknow.append(spell)

    #Actions
    @staticmethods
    def castSpell(ch1, ch2, spell):
        """
        expand spell slots
        """

    @staticmethods
    def weaponattack(ch1, ch2, weapon):
        self.weapons[weaponnum].attack() + self.proficiencyBonus

    def useItem(self, itemnum):
        self.item[itemnum].use()

    def move(self, displacement):

    #items/Weapons/Armor
    def getIteem(self, item):
        self.items.append(item)

    def dropItem(self,item):
        self.items.remove(item)

    def getWeapon(self, weapon):
        self.weapons.append(weapon)

    def dropWeapon(self,weapon):
        self.weapons.remove(weapon)

    def setArmor(self, armor):
        self.armor = str("armor")
        self.armor.set()

    #Save/Load Charcters to text file
    def savecharacter(self):
        """
        writes the characters current stats into a textfile to be loaded in subsequent sessions
        """

    def loadcharacter(self):


    #MISC.
    def roll(d):
        print(str(random.randint(1,d)))

    def str(self):

    def netWorth(self):
        """
        from self.items reads and sums the value of each item object
        """

class Class(object):
    """
    classes
    """
    def __init__(self, class):
        self.class = str()
        self.classLevel = 1
        self.spellList = []
        self.initalHitpoint = 0
        self.hitpointPerlevel = 0
        self.savingThrows = []
        self.spellcastingmod = str()

    def addClass(self):


class Race(object):
    def __init__(self, name, size):
        self.class = str(name)
        self.size = size

    def addRace(self):

class Spell(object):
    def __init__(self,name, dmg, heal, rank):
        self.name = str(name)
        self.dmg = dmg
        self.heal = heal
        self.rank = rank

    def addSpell(self):

    def cast(self):

class Item(object):
    def __init__(self, name, value):
        self.name = str(name)
        self.value = value #in some units

    def addItem(self):

    def use(self):


class Weapon(object):
    def __init__(self, name, damagedice, abilitymod):
        self.name = str(name)
        self.damagedice = damagedice
        self.mod = str(abilitymod)
        self.reach = 5

    def addWeapon(self):

    def attack(self):


class Armor(object):
    def __init__(self, name, baseAC, dexmodmax):
        self.name = str(name)
        self.baseAC = baseAC
        self.dexmodmax = dexmodmax

    def addArmor(self):

    def equip(self):


class effect(objecy):
    def __init__(self):
        self.name = str(name)

    def AddEffect(self):

"""
class deathroll(object):
    def __init__(self):
        self.prob = [.05, .45, .45, .05]
        self.elements = ["F", "f", "p", "P"]
        self.numelem = len(self.elements)
        self.savevalue = [0, 0, 1, 3]
        self.failvalue = [2, 1, 0, 0]
        self.name = str()
        self.end = "cont."
        self.save = 0
        self.fail = 0
        self.chance = 1.
        self.branch = []

    def str(self):
        print(self.name, self.end, self.chance)

    def roll(self, i):
        if self.end == "cont.":
            self.name = np.core.defchararray.add(self.name, self.elements[i])
            self.save += self.savevalue[i]
            self.fail += self.failvalue[i]
            self.chance = self.chance*self.prob[i]
            self.check()

    def check(self):
        if self.save >= 3:
            self.end = "Save"
            print("Saved")
        if self.fail >= 3:
            self.end = "Fail"
            print("Failed")

    def initialize(self, i):
        self.name = self.elements[i]
        self.save = self.savevalue[i]
        self.fail = self.failvalue[i]
        self.chance = self.prob[i]
        self.check()
        self.getBranch()

    def getBranch(self):
        for i in range(self.numelem):
            possout = copy.deepcopy(self)
            possout.roll(i)
            self.branch.append(possout)
            if possout.end == "cont.":
                possout.getBranch()
            possout.printBranch()

    def wholeBranch(self):
        for i in range(len(self.branch)):
            if self.branch[i].end == "cont.":
                self.branch[i].getBranch()
                for j in self.branch[i].branch:
                    self.branch.append(self.branch[i].branch[j])

    def getBranch(self):
        outcomes = []
        for i in range(self.numelem):
            possout = copy.deepcopy(self)
            possout.roll(i)
            outcomes.append(possout)
        self.branch = outcomes


    def printBranch(self):
        for i in range(len(self.branch)):
            self.branch[i].str()
    """
