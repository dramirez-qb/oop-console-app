from src.robot import Robot

# Note: This class is ambiguous. 
# I just added the procedure time to the list of robots

class Procedure:
    time = 0
    robots = [Robot]

    def __init__(self, time, robots) -> None:
        self.time = time
        self.robots = robots

    def update_time(self):
        for i in self.robots:
            i.add_time(self.time)
