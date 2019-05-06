from player_class import Player
from python_to_db_connection import *

class Pokemon:
    def __init__(self):
        self.pokemon_name = ''

    def pokemon_tackle(self):
        pass

    def make_sound_speak(self):
        pass

    def rest_regain_health(self):
        pass

    def save_pokemon(self, xyz):
        a_pokemon = Player('','')
        a_pokemon.search_for_pokemon('')


        try:
            query = (f"INSERT INTO Pokemon (pokemon_name)"
                     f" VALUES ('{xyz}' )")

            cursor.execute(query)
            pokemon_db.commit()

            print("\nPokemon Table updated, 1 row affected.")

        except Exception as ermsg:
            print("\nPânico !! ! !!")
            print(ermsg)
            raise


    def load_a_pokemon(self):
        pass