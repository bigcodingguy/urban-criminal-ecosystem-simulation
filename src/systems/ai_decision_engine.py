import random
from models.organization import Organization

""" Luce-based weighted stochastic decision engine for organizational action selection.

Each organization has one of four personality types, each defined by a weight
vector over the six possible weekly actions. The choose_action function normalizes
weights into probabilities and selects from them. Personality is set at organization
creation and stays the same.

"""

possible_actions = ['Expand', 'Recruit', 'Establish', 'Attack', 'Negotiate', 'Lay Low']
personality_weights = {
    'Opportunistic': {'Expand': 8, 'Recruit': 6, 'Establish': 7, 'Attack': 8, 'Negotiate': 4, 'Lay Low': 4},
    'Territorial': {'Expand': 10, 'Recruit': 8, 'Establish': 6, 'Attack': 4, 'Negotiate': 6, 'Lay Low': 3},
    'Vindictive': {'Expand': 6, 'Recruit': 7, 'Establish': 6, 'Attack': 8, 'Negotiate': 5, 'Lay Low': 4},
    'Strategic': {'Expand': 6, 'Recruit': 8, 'Establish': 8, 'Attack': 5, 'Negotiate': 6, 'Lay Low': 6}
}

def choose_action(personality):
    weights = personality_weights[personality]
    total = 0
    for value in weights.values():
        total += value

    roll = random.random()
    probabilities = 0
    for action, weight in weights.items():
        probabilities += weight / total
        if roll < probabilities:
            return action