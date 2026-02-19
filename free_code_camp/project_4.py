from collections import defaultdict


class HashTable:
    def __init__(self):
        self.collection: dict[int, dict] = defaultdict(dict)

    @staticmethod
    def hash(param: str) -> int:
        return sum(map(ord, param))

    def add(self, key: str, value):
        self.collection[self.hash(key)][key] = value

    def remove(self, key: str):
        if (h := self.hash(key)) in self.collection and key in self.collection[h]:
            del self.collection[h][key]

    def lookup(self, key: str):
        return self.collection.get(self.hash(key), {}).get(key, None)
