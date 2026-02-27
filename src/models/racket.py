class Racket:
    def __init__(self, type, base_income, heat_generated):
        self.type = type
        self.territory = None
        self.base_income = base_income
        self.heat_generated = heat_generated
        self.is_operational = True

    def calculate_income(self):
        if self.is_operational:
            return self.base_income
        else:
            return 0