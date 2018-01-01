from random import randint

class Attributes:
    saving_throws = dict()
    skills = dict()

    def __init__(self):
        self.saving_throws["strength"] = 1
        self.saving_throws["dexterity"] = 1
        self.saving_throws["constitution"] = 1
        self.saving_throws["intelligence"] = 1
        self.saving_throws["wisdom"] = 1
        self.saving_throws["charisma"] = 1

        self.skills["acrobatics"] = 0
        self.skills["animal_handling"] = 0
        self.skills["arcana"] = 0
        self.skills["athletics"] = 0
        self.skills["deception"] = 0
        self.skills["history"] = 0
        self.skills["insight"] = 0
        self.skills["intimidation"] = 0
        self.skills["investigation"] = 0
        self.skills["medicine"] = 0
        self.skills["nature"] = 0
        self.skills["perception"] = 0
        self.skills["performance"] = 0
        self.skills["persuasion"] = 0
        self.skills["religion"] = 0
        self.skills["sleight_of_hand"] = 0
        self.skills["stealth"] = 0
        self.skills["survival"] = 0

class DNDCharacter:
    attribute = Attributes()
    description = dict()
    description["name"] = str()
    description["background"] = str()
    description["initiative"] = int()
    description["current_hp"] = int()
    description["max_hp"] = int()
    description["hitdie"] = 20

    def calculateSavingThrow(self,value):
        compare = int(value)
        print(compare)
        if (compare == 1):
            return -5
        elif(compare >= 2 and compare < 4):
            return -4
        elif(compare >= 4 and compare < 6):
            return -3
        elif(compare >= 6 and compare < 8):
            return -2
        elif(compare >= 8 and compare < 10):
            return -1
        elif(compare >= 10 and compare < 12):
            return 0
        elif(compare >= 12 and compare < 14):
            return 1
        elif(compare >= 14 and compare < 16):
            return 2
        elif(compare >= 16 and compare < 18):
            return 3
        elif(compare >= 18 and compare < 20):
            return 4
        elif(compare >= 20 and compare < 22):
            return 5
        elif(compare >= 22 and compare < 24):
            return 6
        elif(compare >= 24 and compare < 26):
            return 7
        elif(compare >= 26 and compare < 28):
            return 8
        elif(compare >= 28 and compare < 30):
            return 9
        elif(compare == 30):
            return 10

    def setAttribute(self,key : str,value):
        if (key in self.attribute.saving_throws):
            self.attribute.saving_throws[key] = value
            self.calculateSkills()
        elif (key in self.description):
            self.description[key] = value
        else:
            return str("Error : " + " attribute (" + key + ") not found")
    
    def getAttribute(self,key : str):
        if (key in self.attribute.saving_throws):
            return self.attribute.saving_throws[key]
        elif (key in self.description):
            return self.description[key]
        elif (key in self.attribute.skills):
            return self.attribute.skills[key]
        else:
            return str("Error : " + "attribute (" + key + ") not found")
    
    def calculateSkills(self):
        self.attribute.skills["athletics"] = self.calculateSavingThrow(self.attribute.saving_throws["strength"])
        self.attribute.skills["acrobatics"] = self.calculateSavingThrow(self.attribute.saving_throws["dexterity"])
        self.attribute.skills["sleight_of_hand"] = self.calculateSavingThrow(self.attribute.saving_throws["dexterity"])
        self.attribute.skills["arcana"] = self.calculateSavingThrow(self.attribute.saving_throws["intelligence"])
        self.attribute.skills["history"] = self.calculateSavingThrow(self.attribute.saving_throws["intelligence"])
        self.attribute.skills["nature"] = self.calculateSavingThrow(self.attribute.saving_throws["intelligence"])
        self.attribute.skills["religion"] = self.calculateSavingThrow(self.attribute.saving_throws["intelligence"])
        self.attribute.skills["animal_handling"] = self.calculateSavingThrow(self.attribute.saving_throws["wisdom"])
        self.attribute.skills["insight"] = self.calculateSavingThrow(self.attribute.saving_throws["wisdom"])
        self.attribute.skills["medicine"] = self.calculateSavingThrow(self.attribute.saving_throws["wisdom"])
        self.attribute.skills["perception"] = self.calculateSavingThrow(self.attribute.saving_throws["wisdom"])
        self.attribute.skills["survival"] = self.calculateSavingThrow(self.attribute.saving_throws["wisdom"])
        self.attribute.skills["deception"] = self.calculateSavingThrow(self.attribute.saving_throws["charisma"])
        self.attribute.skills["intimidation"] = self.calculateSavingThrow(self.attribute.saving_throws["charisma"])
        self.attribute.skills["performance"] = self.calculateSavingThrow(self.attribute.saving_throws["charisma"])
        self.attribute.skills["persuasion"] = self.calculateSavingThrow(self.attribute.saving_throws["charisma"])
        self.description["max_hp"] = self.description["hitdie"] + self.calculateSavingThrow(self.attribute.saving_throws["constitution"])


class DNDGame:
    character = dict()
    
    def addCharacter(self,name):
        self.character[name] = DNDCharacter()
    
    def getCharacter(self,name):
        if name in self.character:
            return self.character[name]
        else:
            return None
    
    def deleteCharacter(self,name):
        if name in self.character:
            del self.character[name]

    def rollDice(self,min,max):
        return randint(min,max)
    
    def rollD20(self):
        return randint(1,20)

    def rollD6(self):
        return randint(1,6)

    def getModified(self,value : int):
        compare = int(value)
        if (compare == 1):
            return -5
        elif(compare >= 2 and compare < 4):
            return -4
        elif(compare >= 4 and compare < 6):
            return -3
        elif(compare >= 6 and compare < 8):
            return -2
        elif(compare >= 8 and compare < 10):
            return -1
        elif(compare >= 10 and compare < 12):
            return 0
        elif(compare >= 12 and compare < 14):
            return 1
        elif(compare >= 14 and compare < 16):
            return 2
        elif(compare >= 16 and compare < 18):
            return 3
        elif(compare >= 18 and compare < 20):
            return 4
        elif(compare >= 20 and compare < 22):
            return 5
        elif(compare >= 22 and compare < 24):
            return 6
        elif(compare >= 24 and compare < 26):
            return 7
        elif(compare >= 26 and compare < 28):
            return 8
        elif(compare >= 28 and compare < 30):
            return 9
        elif(compare == 30):
            return 10

