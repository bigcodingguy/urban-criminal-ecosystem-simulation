import csv
import matplotlib.pyplot as plt

""" Per-run figure generator for named scenarios.

Reads per-week CSVs produced by main.py and generates three figures
per run (treasury, member count, territory count over time), one
line per organization. Output is saved as PNGs in data/

"""

run_names = {
    1: 'Baseline',
    2: 'Crowded but Poor',
    3: 'Rich but Sparse',
    4: 'Police State',
    5: 'Two Orgs',
    6: 'Max Orgs Crowded',
    7: 'No Police',
    8: 'Maximum Police',
    9: 'Long Run (50 weeks)',
    10: 'Very Long Run (100 weeks)'
}
data = {}
for run_id in range(1, 11):
    data.clear()
    with open(f'data/run_{run_id}.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            week = int(row[0])
            organization = row[1]
            treasury = float(row[2])
            if organization not in data:
                data[organization] = {'weeks': [], 'treasury': []}
            data[organization]['weeks'].append(week)
            data[organization]['treasury'].append(treasury)

    for org in data:
        plt.plot(data[org]['weeks'], data[org]['treasury'], label=org)
    plt.xlabel('Week')
    plt.ylabel('Treasury')
    plt.title('Treasury Over Time')
    plt.legend()
    plt.savefig(f'data/run_{run_id}_treasury.png')
    plt.close()
    data.clear()

    with open(f'data/run_{run_id}.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            week = int(row[0])
            organization = row[1]
            members = int(row[3])
            if organization not in data:
                data[organization] = {'weeks': [], 'members': []}
            data[organization]['weeks'].append(week)
            data[organization]['members'].append(members)

    for org in data:
        plt.plot(data[org]['weeks'], data[org]['members'], label=org)
    plt.xlabel('Week')
    plt.ylabel('Members')
    plt.title('Member Count Over Time')
    plt.legend()
    plt.savefig(f'data/run_{run_id}_members.png')
    plt.close()
    data.clear()

    with open(f'data/run_{run_id}.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            week = int(row[0])
            organization = row[1]
            territories = int(row[4])
            if organization not in data:
                data[organization] = {'weeks': [], 'territories': []}
            data[organization]['weeks'].append(week)
            data[organization]['territories'].append(territories)

    for org in data:
        plt.plot(data[org]['weeks'], data[org]['territories'], label=org)
    plt.xlabel('Week')
    plt.ylabel('Territories')
    plt.title('Territory Count Over Time')
    plt.legend()
    plt.savefig(f'data/run_{run_id}_territories.png')
    plt.close()