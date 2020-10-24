import json


def sort_managers(data):
    dict_managers = {}
    for p, project in enumerate(data):
        for m, manager in enumerate(project['managers']):
            if not manager in dict_managers:
                dict_managers[str(manager)] = {}
                dict_managers[str(manager)][project['name']] = project['priority']
            else:
                dict_managers[str(manager)][project['name']] = project['priority']

    for n, man in enumerate(dict_managers):
        sort_orders = [key for (key, value) in sorted(
            dict_managers[man].items(), key=lambda x: x[1])]
        dict_managers[man] = sort_orders

    json_object = json.dumps(dict_managers, indent=4)
    with open("managers.json", "w") as outfile:
        outfile.write(json_object)


def sort_watchers(data):
    dict_watchers = {}
    for p, project in enumerate(data):
        for m, watcher in enumerate(project['watchers']):
            if not watcher in dict_watchers:
                dict_watchers[str(watcher)] = {}
                dict_watchers[str(watcher)][project['name']] = project['priority']
            else:
                dict_watchers[str(watcher)][project['name']] = project['priority']

    for n, man in enumerate(dict_watchers):
        sort_orders = [key for (key, value) in sorted(
            dict_watchers[man].items(), key=lambda x: x[1])]
        dict_watchers[man] = sort_orders

    json_object = json.dumps(dict_watchers, indent=4)
    with open("watchers.json", "w") as outfile:
        outfile.write(json_object)


def main():
    f = open('source_file_2.json',)
    data = json.load(f)
    sort_managers(data)
    sort_watchers(data)
    f.close()


if __name__ == '__main__':
    main()
