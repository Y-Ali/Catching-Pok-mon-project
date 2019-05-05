from pokemonNames.pokemonNames import PokemonNames

class Player:

    def __init__(self):
        self.name = ''
        self.city = ''
        self.caught_pokemon = []

    def search_for_pokemon(self):
        call_pokemon = PokemonNames()
        get_random_pokemon_name = call_pokemon.get_random_name()

        # print(get_random_pokemon_name)
        # print(self.name)

        asked = False
        while not asked:
            user_name = input("Hi!, What's your name? > ")
            self.name = user_name
            asked = True
            print("generated Pokémon  ----->", get_random_pokemon_name)

            self.__try_to_catch_pokemon(get_random_pokemon_name)

    def __try_to_catch_pokemon(self, get_random_pokemon_name):
        asked = False
        while not asked:
            capture_pokemon = input("Do you want to try and capture a Pokémon!? y/n > ")
            if capture_pokemon == "y":
                print("We've found a", get_random_pokemon_name, "!")

    def save_player_and_pokemon(self):
        pass


    def load_previous_player(self):
        pass
