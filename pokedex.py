from database import Database
from writeAJson import writeAJson


class pokedex:
    def __init__(self):
        self.db = Database(database="pokedex", collection="pokemons")
        self.db.resetDatabase()

    def getPokemonByName(self, name: str):
        return self.db.collection.find({"name": name})

    def getPokemonsByType(self, types: list):
        return self.db.collection.find({"type": {"$in": types}})

    def onlyOneWeakness(self):
        return self.db.collection.find({"weaknesses": {"$size": 1}})

    def lowSpawnRate(self):
        return self.db.collection.find({"spawn_chance": {"$gt": 0.3, "$lt": 0.6}})

    def noMutl(self):
        return self.db.collection.find({"multipliers": None})
