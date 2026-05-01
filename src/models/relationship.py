""" Relationship class tracking the relational state between two organizations.

Each relationship pairs two organizations and maintains a current state
between them, spanning Alliance to War, plus a history of all historical states.
Updates are made via Markov transitions in the simulation loop.

"""

class Relationship:
    def __init__(self, org_a, org_b, state):
        self.org_a = org_a
        self.org_b = org_b
        self.state = state
        self.history = []

    def update(self, new_state):
        self.state = new_state
        self.history.append(new_state)