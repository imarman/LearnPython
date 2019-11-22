import json

mapping = {'a': 32, 'b': 42, 'c': 0xc0ffee}
result = json.dumps(mapping, indent=4, sort_keys=True)
print(result)