from database import Database
from helper.WriteAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")

pokemon = db.collection.find_one({"name" : "Bulbasaur"})


writeAJson(pokemon, "pokemon")
