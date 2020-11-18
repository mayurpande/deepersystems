import os
import json

# Open source file
with open('source_file_2.json', 'r') as f:
    data = json.load(f)

# Sort according to priority
sorted_pri = sorted(data, key=lambda k: k['priority'])

# Loop content and create content
managers = {}
watchers = {}

for item in sorted_pri:
    for key, value in item.items():
        if 'managers' in key:
            for manager in value:
                if manager not in managers.keys():
                    managers[manager] = [item['name']]
                else:
                    managers[manager].append(item['name'])

        elif 'watchers' in key:
            for watcher in value:
                if watcher not in watchers.keys():
                    watchers[watcher] = [item['name']]
                else:
                    watchers[watcher].append(item['name'])

# Write to files
with open(os.getcwd() + '/managers.json', 'w') as f:
    json.dump(managers, f)

with open(os.getcwd() + '/watchers.json', 'w') as f:
    json.dump(watchers, f)


