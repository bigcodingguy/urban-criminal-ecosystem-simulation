from models.member import Member
from models.territory import Territory
from models.racket import Racket

class Organization:
    def __init__(self, name, treasury, heat, hq, leader, personality):
        self.name = name
        self.treasury = treasury
        self.heat = heat
        self.members = []
        self.territories = []
        self.rackets = []
        self.hq = hq
        self.leader = leader
        self.personality = personality
        self.is_player = False
        self.is_active = True

    def collect_income(self):
        for racket in self.rackets:
            self.treasury += racket.calculate_income()
        for territory in self.territories:
            self.treasury += int(territory.income_value * (territory.control_requirement / 2) * 0.3)
        return self.treasury
    
    def pay_expenses(self):
        sorted_members = sorted(self.members, key=lambda m: m.skill, reverse=True)
        money_left = self.treasury
        unpaid_members = 0
        for member in sorted_members:
            if money_left >= member.wage:
                money_left -= member.wage
            else:
                member.update_loyalty(-10)
                unpaid_members += 1
        if unpaid_members > 0:
            print(f"{self.name} skipped {unpaid_members} paychecks this week. Loyalty wavers.")
        self.treasury = money_left
    
    def recruit_members(self, new_members):
        for member in new_members:
            self.members.append(member)

    def allocate_members(self):
        return
    
    def choose_action(self):
        if self.is_player:
            return None # player chooses via input
        else:
            pass # TODO AI decisions

    def calculate_heat_delta(self, delta):
        if (self.heat + delta) > 100:
            self.heat = 100
        elif (self.heat + delta) < 0:
            self.heat = 0
        else:
            self.heat += delta
        return self.heat
    
    def get_controlled_assets(self):
        return self.territories
    
    def has_asset_type(self, type):
        for territory in self.territories:
            if territory.asset_subtype == type:
                return True
        else:
            return False
        
    def eliminate(self):
        for territory in self.territories:
            territory.owner = None
        self.territories.clear()
        self.members.clear()
        self.rackets.clear()
        self.treasury = 0
        self.is_active = False
