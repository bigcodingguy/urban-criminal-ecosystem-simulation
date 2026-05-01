from simulation import Simulation
import statistics
import csv
import math
import matplotlib.pyplot as plt

""" Statistical analysis for sensitivity analysis, scenarios, and extreme condition tests.

Runs ~990 simulations across five parameters (five values each), four named scenarios,
and six extreme condition tests, all 30 runs each. Aggregates results into mean,
standard deviation, min, max, and 95% confidence interval for four metrics (surviving_orgs,
avg_treasury, avg_heat, top_share) and prints to terminal. Generates a six-subplot grid.

"""

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

sensitivity_parameters = {
    'num_orgs': [3, 5, 6, 7, 8],
    'starting_treasury': [500, 1000, 2000, 3500, 5000],
    'members_per_org': [2, 4, 6, 8, 10],
    'num_territories': [8, 12, 16, 20],
    'raid_threshold': [30, 50, 70, 90]
}

scenarios = {}
scenarios['normal'] = baseline

crowded_but_poor = baseline.copy()
crowded_but_poor['num_orgs'] = 8
crowded_but_poor['starting_treasury'] = 500
crowded_but_poor['num_territories'] = 12
scenarios['crowded_but_poor'] = crowded_but_poor

rich_but_sparse = baseline.copy()
rich_but_sparse['num_orgs'] = 3
rich_but_sparse['starting_treasury'] = 5000
rich_but_sparse['members_per_org'] = 8
rich_but_sparse['raid_threshold'] = 80
scenarios['rich_but_sparse'] = rich_but_sparse

police_state = baseline.copy()
police_state['raid_threshold'] = 30
scenarios['police_state'] = police_state

extreme_conditions = {}
two_orgs = baseline.copy()
two_orgs['num_orgs'] = 2
extreme_conditions['two_orgs'] = two_orgs

max_orgs_crowded = baseline.copy()
max_orgs_crowded['num_orgs'] = 8
max_orgs_crowded['num_territories'] = 8
extreme_conditions['max_orgs_crowded'] = max_orgs_crowded

no_police = baseline.copy()
no_police['raid_threshold'] = 100
extreme_conditions['no_police'] = no_police

maximum_police = baseline.copy()
maximum_police['raid_threshold'] = 0
extreme_conditions['maximum_police'] = maximum_police

long_run = baseline.copy()
long_run['num_weeks'] = 50
extreme_conditions['long_run'] = long_run

very_long_run = baseline.copy()
very_long_run['num_weeks'] = 100
extreme_conditions['very_long_run'] = very_long_run




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

def run_analysis():
    results = {}
    for parameter, values in sensitivity_parameters.items():
        results[parameter] = {}
        for value in values:
            config = baseline.copy()
            config[parameter] = value

            runs = []
            for i in range(num_runs):
                runs.append(run_sim(config, i))
            
            stats = aggregate_runs(runs)
            inner_dict = results[parameter]
            inner_dict[value] = stats
    return results

def run_scenarios():
    results = {}
    for scenario, config in scenarios.items():
        runs = []
        for i in range(num_runs):
            runs.append(run_sim(config, i))
        
        stats = aggregate_runs(runs)
        results[scenario] = stats

    return results

def run_extremes():
    results = {}
    for extreme, config in extreme_conditions.items():
        runs = []
        for i in range(num_runs):
            runs.append(run_sim(config, i))
        
        stats = aggregate_runs(runs)
        results[extreme] = stats

    return results

def print_analysis(results):
    for parameter, values in results.items():
        print(f"--- {parameter} ---")
        for value, metrics in values.items():
            print(f"  value = {value}")
            for metric, stats in metrics.items():
                print(f"    {metric}: mean={stats['mean']}, standard deviation={stats['std']}, min={stats['minimum']}, max={stats['maximum']}, confidence interval=[{stats['ci_low']}, {stats['ci_high']}]")
        
def print_scenarios(results):
    for scenario, metrics in results.items():
        print(f"--- {scenario} ---")
        for metric, stats in metrics.items():
            print(f"  {metric}: mean={stats['mean']}, standard deviation={stats['std']}, min={stats['minimum']}, max={stats['maximum']}, confidence interval=[{stats['ci_low']}, {stats['ci_high']}]")

def plot_sensitivity(results):
    figure, axes = plt.subplots(2, 3, figsize=(14, 8))
    axes = axes.flatten()
    x = list(results['num_orgs'].keys())
    y = []
    for value in x:
        y.append(results['num_orgs'][value]['surviving_orgs']['mean'])
    axes[0].plot(x, y)
    axes[0].set_title('num_orgs vs surviving_orgs')
    axes[0].set_xlabel('num_orgs')
    axes[0].set_ylabel('surviving_orgs')

    x = list(results['starting_treasury'].keys())
    y = []
    for value in x:
        y.append(results['starting_treasury'][value]['surviving_orgs']['mean'])
    axes[1].plot(x, y)
    axes[1].set_title('starting_treasury vs surviving_orgs')
    axes[1].set_xlabel('starting_treasury')
    axes[1].set_ylabel('surviving_orgs')

    x = list(results['members_per_org'].keys())
    y = []
    for value in x:
        y.append(results['members_per_org'][value]['surviving_orgs']['mean'])
    axes[2].plot(x, y)
    axes[2].set_title('members_per_org vs surviving_orgs')
    axes[2].set_xlabel('members_per_org')
    axes[2].set_ylabel('surviving_orgs')

    x = list(results['num_territories'].keys())
    y = []
    for value in x:
        y.append(results['num_territories'][value]['surviving_orgs']['mean'])
    axes[3].plot(x, y)
    axes[3].set_title('num_territories vs surviving_orgs')
    axes[3].set_xlabel('num_territories')
    axes[3].set_ylabel('surviving_orgs')

    x = list(results['raid_threshold'].keys())
    y = []
    for value in x:
        y.append(results['raid_threshold'][value]['avg_heat']['mean'])
    axes[4].plot(x, y)
    axes[4].set_title('raid_threshold vs avg_heat')
    axes[4].set_xlabel('raid_threshold')
    axes[4].set_ylabel('avg_heat')

    x = list(results['raid_threshold'].keys())
    y = []
    for value in x:
        y.append(results['raid_threshold'][value]['avg_treasury']['mean'])
    axes[5].plot(x, y)
    axes[5].set_title('raid_threshold vs avg_treasury')
    axes[5].set_xlabel('raid_threshold')
    axes[5].set_ylabel('avg_treasury')

    plt.tight_layout()
    plt.savefig('data/sensitivity_plot.png')
    plt.close()

print("Running sensitivity analysis...")
sensitivity_results = run_analysis()

print("\nRunning scenarios...")
scenario_results = run_scenarios()

print("\nRunning extreme conditions...")
extreme_results = run_extremes()

print("\n----- Sensitivity Results -----")
print_analysis(sensitivity_results)

print("\n----- Scenario Results -----")
print_scenarios(scenario_results)

print("\n----- Extreme Condition Results -----")
print_scenarios(extreme_results)

plot_sensitivity(sensitivity_results)