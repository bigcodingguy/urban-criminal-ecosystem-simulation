import random
from models.organization import Organization
from models.member import Member
from models.territory import Territory

""" Lanchester-based probabilistic conflict resolution between two organizations.

Computes attacker and defender forces as a sum of per-member strength (skill + loyalty + random variant),
with a 1.5x multiplier for defenders. The winner is determined probabilistically and casualties are
assigned based on per-member rolls impacted by skill and the difference in force. If an attack is
successful, a territory is transferred from loser to winner.

"""

def calculate_force(organization, modifier):
    total = 0
    for member in organization.members:
        total += member.skill * (member.loyalty / 100) * random.uniform(0.5, 1.5)

    return total * modifier

def resolve_combat(attacker, defender, territory):
    attacker_force = calculate_force(attacker, 1.0)
    defender_force = calculate_force(defender, 1.5)

    attacker_win_probability = attacker_force / (attacker_force + defender_force)

    roll = random.random()
    if roll < attacker_win_probability:
        winner = attacker
        loser = defender
        winner.territories.append(territory)
        loser.territories.remove(territory)
        territory.change_owner(winner)
    else:
        winner = defender
        loser = attacker
    
    dead = []
    for member in winner.members:
        divisor = (member.skill / 100) + (member.loyalty / 100)
        death_probability = 0.1 / divisor
        casualty_roll = random.random()
        if casualty_roll < death_probability:
            dead.append(member)

    for member in dead:
        winner.members.remove(member)
    
    winner_casualties = len(dead)
    dead.clear()

    for member in loser.members:
        divisor = (member.skill / 100) + (member.loyalty / 100)
        death_probability = 0.2 / divisor
        casualty_roll = random.random()
        if casualty_roll < death_probability:
            dead.append(member)

    for member in dead:
        loser.members.remove(member)

    loser_casualties = len(dead)
    return winner, winner_casualties, loser_casualties