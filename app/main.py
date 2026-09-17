from app.players.player import Player
from app.players.dwarves.dwarf import Dwarf
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.elves.elf import Elf
from app.players.elves.elf_ranger import ElfRanger
from app.players.elves.druid import Druid

def calculate_team_total_rating(players: list[Player]) -> int:
    sum_ratings = 0
    for player in players:
        sum_ratings += player.get_rating()
    return sum_ratings


def elves_concert(players: list[Elf]) -> None:
    for player in players:
        player.play_elf_song()


def feast_of_the_dwarves(players: list[Dwarf]) -> None:
    for player in players:
        player.eat_favourite_dish()
