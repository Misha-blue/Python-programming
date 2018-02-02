import os
import json
import tempfile
import argparse

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')


def main():
    storage_realisation()


def storage_realisation():
    if not os.path.isfile(storage_path):
        with open(storage_path, 'w') as f:
            f.write("")
    key, val = get_arguments()
    dictionary(key=key, val=val)


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--key")
    parser.add_argument("--val", default=None)
    results = parser.parse_args()
    return results.key, results.val


def dictionary(key, val):
    json_dict = {}

    with open(storage_path, 'r') as json_file:
        if os.path.getsize(storage_path) > 0:
            json_str = json.load(json_file)
            json_dict = json.loads(json_str)

    if val is None:
        values = json_dict.get(key)
        if values is not None:
            print(', '.join(values))

    else:
        json_dict.setdefault(key, []).append(val)
        json_dict = json.dumps(json_dict)
        with open(storage_path, 'w') as json_file:
            json.dump(json_dict, json_file)
    return json_dict


if __name__ == "__main__":
    main()
