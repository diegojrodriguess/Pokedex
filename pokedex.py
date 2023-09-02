from database import Database
from helper.WriteAJson import writeAJson

class Pokedex:
    def __init__(self, database : Database):
        self.db = Database (database="pokedex", collection="pokemons")

    def getPokemonByName(self, name: str):
        return self.db.collection.find({"name": name})
        
    def getPokemonsByType(self, types: list):
        return self.db.collection.find({"type": {"$in": types}})
    
    def getPokemonsByOnlyWeakness (self):
        return self.db.collection.find({"weaknesses": {"$size": 1}})
    
    def getPokemonsWithPsychicAndIceWeakness (self, weakness:list):
        return self.db.collection.find({"weaknesses": {"$all": fraquezas}})
    
    def getPokemonsWithFire (self):
        return self.db.collection.find({"$or": [{"type":"Fire"},{"weaknesses": "Fire"}]})


bd = Database(database="pokedex", collection="pokemons")
pokedex = Pokedex (bd)

pikachu = pokedex.getPokemonByName("Pikachu")
writeAJson(pikachu, "pikachu")
types = ["Fighting"]
pokemons = pokedex.getPokemonsByType(types)
writeAJson(pokemons, "pokemons_by_type")

pokemonswow = pokedex.getPokemonsByOnlyWeakness()
writeAJson (pokemonswow,"pokemons_with_one_weakness")

fraquezas = ["Psychic", "Ice"]
pokfracos = pokedex.getPokemonsWithPsychicAndIceWeakness(fraquezas)
writeAJson (pokfracos,"pokemons_with_weakness_ice_psychic")

pokfogo = pokedex.getPokemonsWithFire()
writeAJson (pokfogo,"pokemons_with_fire")

