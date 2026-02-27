# urban-criminal-ecosystem-simulation

# CS 4632 Modeling and Simulation - Kennesaw State University

A discrete-time, agent-based simulation of territorial competition between criminal organizations in an urban environment.

# Overview

This simulation models 6-8 autonomous organizations competing for control of approximately 60 street-level territories and high-value key assets. Organizations make reasoned decisions about expansion, recruitment, rackets, and inter-organizational relations while managing law enforcement "heat".

# Project Status

- Entity classes Member, Territory, Organization, Racket, Relationship
- Markov chain transition system for relationship dynamics
- Weighted stochastic decision model for AI behavior
- Basic simulation loop running weekly cycles with action and relationship components

# To do

- Combat resolution system
- Event system
- Full five-phase weekly loop
- Interactive player mode
- Economy, intel phases
- Member allocation across territories
- Police raids
- City map
- Racket (key asset) multipliers
- Data visualization

# Changes from M1

- Simplified initial setup with basic simulation loop and only 3 starting organizations.
- Changed 'is_alive', 'is_arrested', 'experience', 'stationed_at' to defaults instead of required "Member" parameters.
- Dropped 'is_at_war' method from "Relationship", given 'state' captures it.
- Instead of "Racket" determining its own operational status, made 'is_operational' a simple boolean flag.
- Changed 'members' and 'territories' to empty lists in "Organization" instead of required parameters.

# Installation

- Python 3 required
- No external dependencies
- To test: clone repo, run python src/main.py

# Project Structure
```
src/
  models/
    member.py
    territory.py
    organization.py
    racket.py
    relationship.py
  systems/
    markov_transitions.py
    ai_decision_engine.py
  simulation.py
  main.py
```

# Acknowledgement

AI was used as a limited aid for debugging assistance and understanding concepts and syntax as per the course AI use policy.

# Author

Blake Hammontree - Kennesaw State University, Department of Computer Science
