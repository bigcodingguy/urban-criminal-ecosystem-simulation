import random
from models.organization import Organization

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