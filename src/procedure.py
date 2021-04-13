from src.robot import Robot


class Procedure:
    time = 0
    robots = [Robot]

    def __init__(self, time, robots) -> None:
        self.time = time
        self.robots = robots

    def update_time(self):
        for i in self.robots:
            i.add_time(self.time)
