from src.robot import Robot


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

    def park_robot(self, robot):
        if self.is_full():
            raise GarageFullException()

        if robot in self.robots:
            raise RobotAlreadyInException()

        self.robots.append(robot)

    def remove_robot(self, robot):
        try:
            self.robots.remove(robot)
        except ValueError:
            return False

    def is_full(self):
        return len(self.robots) > self.capacity
