import csv

def create_csv(filename, restrant):
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = ['NAME', 'COUNT']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'NAME': restrant, 'COUNT': 1})

def read_csv(filename):
    with open(filename, 'r', newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        return list(reader)

def update_csv(list, restrant):
    flag = False
    for row in list:
        if row['NAME'] == restrant:
            row['COUNT'] = int(row['COUNT']) + 1
            flag = True
            break
    if not flag:
        list.append({'NAME': restrant, 'COUNT': 1})
    return list

def write_csv(filename, list):
    fieldnames = ['NAME', 'COUNT']
    with open('ranking.csv', 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(list)

def sort_csv(list):
    return sorted(list, key=lambda x: x['COUNT'], reverse=True)
