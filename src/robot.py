class NoEnergyException(Exception):
    pass


class UnhappyException(Exception):
    pass


class Robot:
    name = ""
    happiness = 0
    energy = 0
    procedure_time = 0
    owner = ""

    MAX_ENERGY = 100
    MAX_HAPPINESS = 50

    def __init__(
        self,
        name: str,
        happiness: int,
        energy: int,
        procedure_time: int,
        owner: str,
    ):
        self.name = name
        self.happiness = happiness
        self.energy = energy
        self.procedure_time = procedure_time
        self.owner = owner

    def __eq__(self, other):
        return self.name == other.name and self.owner == other.owner

    def set_owner(self, owner):
        self.owner = owner

    def add_time(self, time):
        self.procedure_time += time

    def work(self):
        self._perform_action(energy_action=-1, happiness_action=1)

    def talk(self):
        self._perform_action(energy_action=1, happiness_action=1)

    def move(self):
        self._perform_action(energy_action=-1, happiness_action=-1)

    def hibernate(self):
        self._perform_action(energy_action=1, happiness_action=-1)

    def _perform_action(self, energy_action: int, happiness_action: int):
        if self.energy + energy_action < 0:
            raise NoEnergyException()

        if self.happiness + happiness_action < 0:
            raise UnhappyException()

        energy_after_action = self.energy + energy_action
        self.energy = (
            energy_after_action
            if energy_after_action < self.MAX_ENERGY
            else self.MAX_ENERGY
        )

        happiness_after_action = self.happiness + happiness_action
        self.happiness = (
            happiness_after_action
            if happiness_after_action < self.MAX_HAPPINESS
            else self.MAX_HAPPINESS
        )
