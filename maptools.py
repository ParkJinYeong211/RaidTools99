import json

def _reverse_a_map(some_dict) -> dict:
    return {v:k for (k,v) in some_dict.items()}

def gen_chain_map() -> dict:
    with open ("map.json", "r") as mapjson:
        map = json.load(mapjson)
    
    return dict(map, **_reverse_a_map(map))

def gen_RT_map() -> dict:
    map = {str(i):f"RT{str(i+1)}" for i in range(8)}

    return dict(map, **_reverse_a_map(map))

