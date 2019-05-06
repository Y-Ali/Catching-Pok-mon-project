from player_class import Player
from python_to_db_connection import *

class Pokemon:
    def __init__(self):
        self.pokemon_name = ''

    def pokemon_tackle(self):
        pass

    def make_sound_speak(self):
        print("Pika Pika Pikachooooooo ")

    def rest_regain_health(self):
        print("Regaining health, do not disturb...")

    # def save_pokemon(self):
    #     #p = Player()
    #
    #     x = p.all_pokemon
    #
    #     str2 = ','.join(p)
    #     print(p)

        # try:
        #     query2 = (f"INSERT INTO Pokemon (pokemon_name)"
        #              f" VALUES ('{str2}' )")
        #
        #     print(query2)
        #     cursor.execute(query2)
        #     pokemon_db.commit()
        #
        #     print("\nPokemon Table updated, 1 row affected.")
        #
        # except Exception as ermsg:
        #     print("\nPânico !! ! !!")
        #     print(ermsg)
        #     raise


    def load_a_pokemon(self):
        pass