import json
import random

from logic.figure import Figure
from logic.room_manager import RoomManager


def parse_game_config(filepath):
    with open(filepath, "r") as config_file:
        raw_config = json.load(config_file)

        # Load and parse rooms (including distances)
        rooms = raw_config["rooms"]
        room_manager = RoomManager(rooms, raw_config["distances"])

        # Load and parse figures (including random initial placement of figures in rooms)
        figures_names = raw_config["figures"]
        figures = [Figure(f, random.choice(rooms)) for f in figures_names]

        # Load and parse weapons
        weapons = raw_config["weapons"]

        return room_manager, figures_names, figures, weapons
