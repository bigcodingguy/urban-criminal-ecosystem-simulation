from simulation import Simulation

config = {
    'num_territories': 20,
    'num_orgs': 6,
    'members_per_org': 5,
    'starting_treasury': 2000,
    'num_weeks': 20,
    'member_wage': 10
    }
sim = Simulation(config)
sim.run(config['num_weeks'])