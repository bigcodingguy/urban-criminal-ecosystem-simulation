# urban-criminal-ecosystem-simulation

# CS 4632 Modeling and Simulation - Kennesaw State University

A discrete-time, agent-based simulation of territorial competition between criminal organizations in an urban environment.

# Overview

This simulation models autonomous organizations competing for control of a shared environment. Organizations make weekly decisions about expansion, recruitment, rackets, and inter-organizational relations while managing law enforcement "heat".

# Installation

- Python 3 required
- No external dependencies
- git clone https://github.com/bigcodingguy/urban-criminal-ecosystem-simulation.git

# Usage

### Running named scenarios and extreme conditions for visualization

python src/main.py
python src/visualize.py

This produces per-run CSVs and PNGs in 'data/' for the four named scenarios plus six extreme conditions.

### Running statistical analysis

python src/analysis.py

This runs ~990 simulations including sensitivity analysis, scenarios, and extreme conditions. Produces a six plot sensitivity grid and prints aggregate statistics to terminal.

## Configuration

Baseline and scenario parameters are defined in 'src/main.py' and 'src/analysis.py'. Edit the dictionaries at the top of either file to change values. Parameters include:

- 'num_orgs': number of competing organizations
- 'num_territories': number of territories in the system
- 'members_per_org': starting members per organization.
- 'starting_treasury': initial treasury (variable +- 60%)
- 'raid_threshold': heat threshold above which raids may trigger
- 'member_wage': weekly wage per member
- 'num_weeks': simulation duration in weeks

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
  analysis.py
  visualize.py
```

## Output Files

- 'data/run\*\_.csv': per-week state for each run
- 'data/run*\_treasury.png', 'data/run_members.png', 'data/run*\_\_territories.png': visualizations
- 'data/sensitivity_plot.png': six subplot sensitivity grid
- 'data/m5_analysis_final.txt': analysis.py aggregate statistics

# Acknowledgement

AI was used as a limited aid for debugging assistance and understanding concepts and syntax as per the course AI use policy.

# Author

Blake Hammontree - Kennesaw State University, Department of Computer Science
