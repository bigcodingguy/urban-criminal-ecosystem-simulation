class Relationship:
    def __init__(self, org_a, org_b, state):
        self.org_a = org_a
        self.org_b = org_b
        self.state = state
        self.history = []

    def update(self, new_state):
        self.state = new_state
        self.history.append(new_state)