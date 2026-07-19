from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        key_map = self.hashmap[key]

        while timestamp >= 0:
            if timestamp in key_map:
                return key_map[timestamp]
            timestamp -= 1

        return ""