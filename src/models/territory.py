class Territory:
    def __init__(self, name, asset_subtype, income_value, heat_profile, control_requirement, visibility_type, neighborhood):
        self.name = name
        self.asset_subtype = asset_subtype
        self.income_value = income_value
        self.heat_profile = heat_profile
        self.owner = None
        self.control_requirement = control_requirement
        self.garrison = []
        self.visibility_type = visibility_type
        self.neighborhood = neighborhood
        self.adjacent_territories = []

    def get_garrison_strength(self):
        return len(self.garrison)
    
    def is_defended(self):
        if len(self.garrison) == 0:
            return False
        else:
            return True
        
    def change_owner(self, new_owner):
        self.owner = new_owner

