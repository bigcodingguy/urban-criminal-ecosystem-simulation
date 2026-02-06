# urban-criminal-ecosystem-simulation

# CS 4632 Modeling and Simulation - Kennesaw State University

A discrete-time, agent-based simulation of territorial competition between criminal organizations in an urban environment.

# Overview

This simulation models 6-8 autonomous organizations competing for control of approximately 60 street-level territories and high-value key assets. Organizations make reasoned decisions about expansion, recruitment, rackets, and inter-organizational relations while managing law enforcement "heat".

# Core Systems

- **Territory:** Street-level holdings and key assets; organized into neighborhoods
- **Economy:** Three racket types (protection, gambling, smuggling) with various conditions and multipliers
- **Members:** Individuals with loyalty, skill, and role attributes
- **Heat:** Law enforcement pressure modeled as an environmental constraint
- **Inter-Organization Relations:** Markov chain state transitions representing everything from alliance to war

# Technical Details

- **Language:** Python 3
- **Simulation Type:** Discrete-time, agent-based
- **Main Models:** Markov chain state transitions, weighted stochastic decision model, probabilistic conflict resolution

# Project Structure
```
├── src/
│   ├── simulation.py
│   ├── city.py
│   ├── organization.py
│   ├── member.py
│   ├── territory.py
│   ├── racket.py
│   ├── relationship.py
│   ├── combat.py
│   ├── ai_engine.py
│   └── events.py
├── data/
│   └── (simulation output logs)
├── docs/
│   └── (submissions)
├── tests/
│   └── (unit tests)
└── README.md
```

# Author

Blake Hammontree - Kennesaw State University, Department of Computer Science
