import csv
import matplotlib.pyplot as plt

data = {}
for run_id in [1, 9, 10]:
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