
from src.garage import Garage
from src.robot import Robot
from src.procedure import Procedure


class TestClass:
    garage = Garage(3)

    # Create the robots
    r2d2 = Robot("R2D2", 20, 40, 0, "Anakin")
    c3po = Robot("C3PO", 30, 50, 0, "Vader")
    bb8 = Robot("BB8", 10, 45, 0, "Rei")

    # Park the robots
    garage.park_robot(r2d2)
    garage.park_robot(c3po)
    garage.park_robot(bb8)

    # Create procedures
    procedures = [
        Procedure(50, robots=[r2d2, bb8]),
        Procedure(60, robots=[r2d2, c3po]),
        Procedure(100, robots=[r2d2, c3po, bb8]),
        Procedure(150, robots=[bb8]),
        Procedure(200, robots=[r2d2])
    ]

    # Test the capacity of the created garage
    def test_garage(self):
        assert self.garage.capacity == 3

    # Test the robots actions and the manage
    # of the energy and happiness
    def test_robot_move(self):
        self.r2d2.move()
        assert self.r2d2.energy == 39 and self.r2d2.happiness == 19

    def test_robot_work(self):
        self.c3po.work()
        assert self.c3po.energy == 49 and self.c3po.happiness == 31

    def test_robot_hibernate(self):
        self.bb8.hibernate()
        assert self.bb8.happiness == 9 and self.bb8.energy == 46

    # Test that the parked robots are in the garage
    def test_robot_list(self):
        flag = True
        for i in self.garage.robots:
            print(i)
        assert flag == True
