import random
from pokemonNames.pokemonNames import PokemonNames

class Player:

    def __init__(self):
        self.name = ''
        self.city = ''
        self.caught_pokemon = []

    def ask_for_name(self):

        user_name = input("Hi!, What's your name? > ")
        self.name = user_name

        self.search_for_pokemon()

    def search_for_pokemon(self):
        call_pokemon = PokemonNames()
        get_random_pokemon_name = call_pokemon.get_random_name()

        print("generated Pokémon  ----->", get_random_pokemon_name)
        self.__try_to_catch_pokemon(get_random_pokemon_name)

    def __try_to_catch_pokemon(self, get_random_pokemon_name):
        asked = False
        print("We've found a", get_random_pokemon_name, "!")

        while not asked:
            capture_pokemon = input(f"Do you want to try and capture a {get_random_pokemon_name}!? y/n > ")
            if capture_pokemon == "y":
                try_can_catch = random.randint(1,10)

                if try_can_catch % 2 == 0:
                    self.caught_pokemon.append(get_random_pokemon_name)
                    print(f"We caught a{get_random_pokemon_name}!")

                else:
                    print("failed to catch")
            asked = True
        print("This is the list", self.caught_pokemon)

        try_again = input("Would you like to search for another Pokémon?")
        if try_again == "y":
            self.search_for_pokemon()

    def save_player_and_pokemon(self):
        pass

    def load_previous_player(self):
        pass













    def save_player_and_pokemon(self):
        pass


    def load_previous_player(self):
        pass
