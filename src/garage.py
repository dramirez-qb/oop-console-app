from src.robot import Robot


# Own Exceptions
class GarageFullException(Exception):
    pass


class RobotAlreadyInException(Exception):
    pass


class RobotNotFoundException(Exception):
    pass


class Garage:
    capacity = 0
    robots = [Robot]

    def __init__(self, capacity: int):
        self.capacity = capacity

    # Add robot to garage
    def park_robot(self, robot):
        if self.is_full():
            raise GarageFullException()

        if robot in self.robots:
            raise RobotAlreadyInException()

        self.robots.append(robot)

    # Remove robot from the garage
    def remove_robot(self, robot):
        try:
            self.robots.remove(robot)
        except ValueError:
            return False

    # Check if garage is full
    def is_full(self):
        return len(self.robots) > self.capacity
