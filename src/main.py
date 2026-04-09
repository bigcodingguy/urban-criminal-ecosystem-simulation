from simulation import Simulation

configs = []

run1 = {
    'num_territories': 20,
    'num_orgs': 6,
    'members_per_org': 5,
    'starting_treasury': 2000,
    'num_weeks': 20,
    'member_wage': 10,
    'raid_threshold': 50
    }

configs.append(run1)



run_id = 1
for config in configs:
    sim = Simulation(config, run_id)
    sim.run(config['num_weeks'])
    run_id += 1