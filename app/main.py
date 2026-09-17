from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, nickname: str) -> None:
        self.nickname = nickname

    @abstractmethod
    def get_rating(self) -> None:
        pass

    @abstractmethod
    def player_info(self) -> int:
        pass

class Elf(Player):
    def __init__(self, musical_instrument: str) -> None:
        super().__init__(self.nickname)
        self._musical_instrument = musical_instrument

    def play_elf_song(self) -> None:
        print(f"{self.nickname} is playing a song on the \
              {self._musical_instrument}")


class Dwarf(Player):
    def __init__(self, favourite_dish: str) -> None:
        super().__init__(self.nickname)
        self._favourite_dish = favourite_dish

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self._favourite_dish}") 

    def player_info(self) -> None:
            print(f'"Elf ranger {self.nickname}. {self.nickname} has bow \
                  of the {self.bow_level} level"` for `ElfRanger` instances"')       


class ElfRanger(Elf):
    def __init__(self, bow_level: int) -> None:
        super().__init__(self.nickname, self._musical_instrument)
        self._bow_level = bow_level

    def player_info(self) -> None:
        print(f'"Elf ranger {self.nickname}. {self.nickname} has bow \
              of the {self.bow_level} level"` for `ElfRanger` instances"')    

    def get_rating(self) -> int:
        return 3 * self._bow_level



class Druid(Elf):
    def __init__(self, favourite_spell: str) -> None:
        super().__init__(self.nickname, self._musical_instrument)
        self._favourite_spell = favourite_spell

    def player_info(self) -> None:
        print(f'"Elf ranger {self.nickname}. {self.nickname} has a \
              favourite spell: {self.favourite_spell}"` for `Druid` instances"')

    def get_rating(self) -> int:
        return len(self._favourite_spell)      


class DwarfWarrior(Dwarf):
    def __init__(self, hummer_level: int ) -> None:
        super().__init__(self.nickname, self._favourite_dish)
        self._hummer_level = hummer_level

    def player_info(self) -> None:
        print(f'"Dwarf warrior {self.nickname}. {self.nickname} has a hummer \
              of the {self.hummer_level} level"` for `DwarfWarrior` instances') 

    def get_rating(self) -> int:
        return self._hummer_level + 4 


class DwarfBlacksmith(Dwarf):
    def __init__(self, skill_level: int ) -> None:
        super().__init__(self.nickname, self._favourite_dish)
        self._skill_level = skill_level

    def player_info(self) -> None:
        print(f'"Dwarf blacksmith {self.nickname} with skill of the \
              {self.skill_level} level"` for `DwarfBlacksmith` instances')

    def get_rating(self) -> int:
        return self._skill_level


def calculate_team_total_rating(players: list[Player]) -> int:
    sum_ratings = 0
    for player in players:
        sum_ratings += player.get_rating
    return sum_ratings    

def elves_concert(players: list[Elf]) -> None:
    for player in players:
        player.play_elf_song()

def elves_concert(players: list[Dwarf]) -> None:
    for player in players:
        player.eat_favourite_dish()
