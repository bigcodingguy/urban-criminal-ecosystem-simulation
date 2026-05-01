""" Racket class representing a profitable criminal operation.

Rackets come in three types (Protection, Gambling, Smuggling),
each with different income, heat generation, and startup costs.
Organiations establish rackets through the Establish action when
they can afford the expense.

"""

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