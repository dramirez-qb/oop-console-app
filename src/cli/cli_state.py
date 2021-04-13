from src.procedure import Procedure
from src.robot import Robot
from src.garage import Garage, RobotNotFoundException


class CliState:
    garage = Garage(0)
    procedures = [Procedure]
    actions_history = []

    def update_garage(self, garage: Garage):
        self.garage = garage

    def update_history(self, data):
        self.actions_history.append(data)

    def get_history(self):
        return self.actions_history

    def get_garage(self):
        return self.garage

    def get_procedures(self):
        return self.procedures

    def get_robots(self):
        return self.garage.robots

    def get_robot_info(self, robot_name, robot_owner):
        for i in self.garage.robots:
            if i.name == robot_name and i.owner == robot_owner:
                return i

        raise RobotNotFoundException

    def remove_robot_from_garage(self, robot_name, robot_owner):
        robot = None

        for i in self.garage.robots:
            if i.name == robot_name and i.owner == robot_owner:
                robot = i

        if robot:
            self.garage.robots.remove(robot)
            return robot
        else:
            raise RobotNotFoundException

    def park_robot(self, robot: Robot):
        self.garage.park_robot(robot)
