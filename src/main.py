from simulation import Simulation

configs = []

run1 = {
    'num_territories': 20,
    'num_orgs': 6,
    'members_per_org': 5,
    'starting_treasury': 2000,
    'num_weeks': 20,
    'member_wage': 10
    }

configs.append(run1)

run2 = {
    'num_territories': 20,
    'num_orgs': 3,
    'members_per_org': 5,
    'starting_treasury': 2000,
    'num_weeks': 20,
    'member_wage': 10
}

configs.append(run2)

run3 = {
    'num_territories': 20,
    'num_orgs': 8,
    'members_per_org': 5,
    'starting_treasury': 2000,
    'num_weeks': 20,
    'member_wage': 10
}

configs.append(run3)

run4 = {
    'num_territories': 20,
    'num_orgs': 6,
    'members_per_org': 5,
    'starting_treasury': 500,
    'num_weeks': 20,
    'member_wage': 10
}

configs.append(run4)

run5 = {
    'num_territories': 20,
    'num_orgs': 6,
    'members_per_org': 5,
    'starting_treasury': 5000,
    'num_weeks': 20,
    'member_wage': 10
}

configs.append(run5)

run6 = {
    'num_territories': 20,
    'num_orgs': 6,
    'members_per_org': 2,
    'starting_treasury': 2000,
    'num_weeks': 20,
    'member_wage': 10
}

configs.append(run6)

run7 = {
    'num_territories': 20,
    'num_orgs': 6,
    'members_per_org': 10,
    'starting_treasury': 2000,
    'num_weeks': 20,
    'member_wage': 10
}

configs.append(run7)

run8 = {
    'num_territories': 20,
    'num_orgs': 8,
    'members_per_org': 5,
    'starting_treasury': 500,
    'num_weeks': 20,
    'member_wage': 10
}

configs.append(run8)

run9 = {
    'num_territories': 20,
    'num_orgs': 3,
    'members_per_org': 5,
    'starting_treasury': 5000,
    'num_weeks': 20,
    'member_wage': 10
}

configs.append(run9)

run10 = {
    'num_territories': 20,
    'num_orgs': 6,
    'members_per_org': 5,
    'starting_treasury': 2000,
    'num_weeks': 50,
    'member_wage': 10
}

configs.append(run10)

run_id = 1
for config in configs:
    sim = Simulation(config, run_id)
    sim.run(config['num_weeks'])
    run_id += 1