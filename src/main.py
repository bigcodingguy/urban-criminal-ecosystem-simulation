from simulation import Simulation

baseline = {
    'num_territories': 20,
    'num_orgs': 6,
    'members_per_org': 5,
    'starting_treasury': 2000,
    'num_weeks': 20,
    'member_wage': 10,
    'raid_threshold': 50
    }

crowded_but_poor = baseline.copy()
crowded_but_poor['num_orgs'] = 8
crowded_but_poor['starting_treasury'] = 500
crowded_but_poor['num_territories'] = 12

rich_but_sparse = baseline.copy()
rich_but_sparse['num_orgs'] = 3
rich_but_sparse['starting_treasury'] = 5000
rich_but_sparse['members_per_org'] = 8
rich_but_sparse['raid_threshold'] = 80

police_state = baseline.copy()
police_state['raid_threshold'] = 30

# Extreme Conditions
two_orgs = baseline.copy()
two_orgs['num_orgs'] = 2

max_orgs_crowded = baseline.copy()
max_orgs_crowded['num_orgs'] = 8
max_orgs_crowded['num_territories'] = 8

no_police = baseline.copy()
no_police['raid_threshold'] = 100

maximum_police = baseline.copy()
maximum_police['raid_threshold'] = 0

long_run = baseline.copy()
long_run['num_weeks'] = 50

very_long_run = baseline.copy()
very_long_run['num_weeks'] = 100

configs = [baseline, crowded_but_poor, rich_but_sparse, police_state, two_orgs, max_orgs_crowded, no_police, maximum_police, long_run, very_long_run]

run_id = 1
for config in configs:
    sim = Simulation(config, run_id)
    sim.run(config['num_weeks'])
    run_id += 1