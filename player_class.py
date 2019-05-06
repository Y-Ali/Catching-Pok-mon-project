import random
from pokemonNames.pokemonNames import PokemonNames
from python_to_db_connection import *

class Player:

    def __init__(self, name, city, caught_pokemon=''):
        self.name = name
        self.city = city
        self.caught_pokemon = []

    def ask_for_name(self):
        user_name = input("Hi!, What's your name? > ")
        city = input("what city are you from? > ")

        self.name = user_name
        self.city = city
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
                    print("---------------------->",self.caught_pokemon)
                else:
                    print("failed to catch")
                    print("---------------------->", self.caught_pokemon)
            asked = True
            print("---------------------->", self.caught_pokemon)
            try_again = input("Would you like to search for another Pokémon?")
            if try_again == "y":
                print("---------------------->", self.caught_pokemon)
                self.search_for_pokemon()
            elif try_again == "n":
                print("---------------------->", self.caught_pokemon)

                self.save_player_and_pokemon(get_random_pokemon_name)


    def save_player_and_pokemon(self, get_random_pokemon_name):
        try:
            if get_random_pokemon_name in self.caught_pokemon:
                print("---------------------->", self.caught_pokemon)

                str1 = ','.join(self.caught_pokemon)

                #print(type(str1))
                #print("entered the if statement.....")

                query = (f"INSERT INTO Player (player_name, city, captured_pokemon)"
                     f" VALUES ('{self.name}', '{self.city}', '{str1}' )")

                print(query)

                cursor.execute(query)
                pokemon_db.commit()

                print("\nTable updated, 1 row affected.")

        except Exception as ermsg:
            print ("\nPânico !! ! !!")
            print(ermsg)
            raise


    def load_previous_player(self):
        try:
            query = ("SELECT * FROM Player")
            player = cursor.execute(query)

            column = cursor.description

            for item in player:
                print(column[0][0]+": " + item.player_name + column[1][0] + ": "
                                        + item.city + column[2][0] + ": " + item.captured_pokemon)
                #break

            print("\nOperation has been completed.")

        except Exception as ermsg:
            print("\nPânico !! ! !! The data has not been read. Please refer to error message.")
            print(ermsg)
            raise

