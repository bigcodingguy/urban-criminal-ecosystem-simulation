from simulation import Simulation
import statistics
import csv
import math
import matplotlib.pyplot as plt

num_runs = 30

baseline = {
    'num_territories': 20,
    'num_orgs': 6,
    'members_per_org': 5,
    'starting_treasury': 2000,
    'num_weeks': 20,
    'member_wage': 10,
    'raid_threshold': 50
}

def run_sim(config, run_id):
    sim = Simulation(config, run_id, log_csv=False, print=False)
    sim.run(config['num_weeks'])
    orgs = 0
    treasury_total = 0
    heat_total = 0
    territory_counts = []

    for org in sim.organizations:
        if org.is_active:
            orgs += 1
            treasury_total += org.treasury
            heat_total += org.heat
            territory_counts.append(len(org.territories))


    if orgs == 0:
        avg_treasury = 0
        avg_heat = 0
    else:
        avg_treasury = round(treasury_total / orgs, 2)
        avg_heat = round(heat_total / orgs, 2)
    
    if territory_counts and sum(territory_counts) > 0:
        top_share = round(max(territory_counts) / sum(territory_counts), 3)
    else:
        top_share = 0

    results = {
        'surviving_orgs': orgs,
        'avg_treasury': avg_treasury,
        'avg_heat': avg_heat,
        'top_share': top_share
    }

    return results

def aggregate_runs(results_list):
    metrics = ['surviving_orgs', 'avg_treasury', 'avg_heat', 'top_share']
    summary = {}
    n = len(results_list)

    for metric in metrics:
        values = []
        for result in results_list:
            values.append(result[metric])
        
        mean = sum(values) / len(values)
        std = statistics.stdev(values)
        minimum = min(values)
        maximum = max(values)
        ci_low = mean - 1.96 * (std / math.sqrt(n))
        ci_high = mean + 1.96 * (std / math.sqrt(n))

        summary[metric] = {
            'mean': round(mean, 2),
            'std': round(std, 2),
            'minimum': round(minimum, 2),
            'maximum': round(maximum, 2),
            'ci_low': round(ci_low, 2),
            'ci_high': round(ci_high, 2)
        }

    return summary