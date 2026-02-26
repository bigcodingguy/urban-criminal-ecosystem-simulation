import random

class Member:
    def __init__(self, name, skill, loyalty, role):
        self.name = name
        self.skill = skill
        self.loyalty = loyalty
        self.role = role
        self.stationed_at = None
        self.is_alive = True
        self.is_arrested = False
        self.experience = 0
    
    def combat_contribution(self):
        return
    
    def update_loyalty(self, x):
        if (self.loyalty + x) > 100:
            self.loyalty = 100
        elif (self.loyalty + x) < 0:
            self.loyalty = 0
        else:
            self.loyalty += x

    def check_betrayal(self):
        if self.loyalty < 10:
            chance = 0.5
        elif self.loyalty < 20:
            chance = 0.25
        elif self.loyalty < 30:
            chance = 0.15
        elif self.loyalty < 40:
            chance = 0.1
        elif self.loyalty < 50:
            chance = 0.05
        else:
            chance = 0.01
        if random.random() < chance:
            return True
        else:
            return False