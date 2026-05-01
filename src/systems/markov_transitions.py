import random
from models.relationship import Relationship

""" Markov chain state transitions for inter-organizational relationships.

A function that, given a current relationship state and a pressure value,
returns a new state via a probability matrix biased toward adjacent state changes.
"""
states = ['Alliance', 'Friendly', 'Neutral', 'Tense', 'Hostile', 'War']

def markov_transition(current_state, event_pressure):
    stay = 0.8
    worsen = 0.1
    improve = 0.1
    if event_pressure > 0.85:
        improve += 0.5
        worsen -= 0.1
        stay -= 0.4
    elif event_pressure > 0.6:
        improve += 0.35
        worsen -= 0.1
        stay -= 0.25
    elif event_pressure > 0.3:
        improve += 0.2
        worsen -= 0.1
        stay -= 0.1
    elif event_pressure > 0:
        improve += 0.05
        worsen -= 0.05
    elif event_pressure < -0.85:
        worsen += 0.5
        improve -= 0.1
        stay -= 0.4
    elif event_pressure < -0.6:
        worsen += 0.35
        improve -= 0.1
        stay -= 0.25
    elif event_pressure < -0.3:
        worsen += 0.2
        improve -= 0.1
        stay -= 0.1
    elif event_pressure < 0:
        worsen += 0.05
        improve -= 0.05
    
    # Update logic
    
    roll = random.random()
    index = states.index(current_state)
    if (roll < improve) and (current_state != 'Alliance'):
        current_state = states[index - 1]
    elif (roll >= improve + stay) and (current_state != 'War'):
        current_state = states[index + 1]

    return current_state