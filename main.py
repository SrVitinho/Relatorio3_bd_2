from database import Database
from writeAJson import writeAJson
from pokedex import pokedex

if __name__ == '__main__':
    pokedex1 = pokedex()
    pikachu = pokedex1.getPokemonByName('Pikachu')
    writeAJson(pikachu, "pikachu")

    types = ["Fighting"]
    pokemons = pokedex1.getPokemonsByType(types)
    writeAJson(pokemons, "pokemons_by_type")

    pokemons = pokedex1.onlyOneWeakness()
    writeAJson(pokemons, "pokemons_only_one")

    pokemons = pokedex1.lowSpawnRate()
    writeAJson(pokemons, "pokemons_low_spawnrate")

    pokemons = pokedex1.noMutl()
    writeAJson(pokemons, "pokemons_no_multipliers")