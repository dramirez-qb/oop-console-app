from src.garage import (
    Garage,
    GarageFullException,
    RobotAlreadyInException,
    RobotNotFoundException,
)
from src.robot import Robot, UnhappyException, NoEnergyException
from src.procedure import Procedure

from .cli_state import CliState
from .commands import Commands
from .invoker import Invoker, CommandNotFoundException


# Console Manager Class
class CliManager:
    def __init__(self):
        # Init state
        self.state = CliState()
        self.populate_data()

        # Register the commands with the invoker
        self.invoker = Invoker()
        self.invoker.register("-1", Commands.start, after_command=None)
        self.invoker.register(
            "1", Commands.create_garage, after_command=self._create_garage
        )
        self.invoker.register(
            "2", Commands.create_robot, after_command=self._create_robot
        )
        self.invoker.register(
            "3", Commands.create_procedure,
            after_command=self._create_procedure
        )
        self.invoker.register(
            "4", Commands.perform_action, after_command=self._perform_action
        )
        self.invoker.register(
            "5", Commands.apply_procedure, after_command=self._apply_procedure
        )
        self.invoker.register(
            "6", Commands.show_history, after_command=self._show_history
        )
        self.invoker.register(
            "7", Commands.show_robot_info, after_command=self._show_robot_info
        )
        self.invoker.register(
            "8", Commands.sell_robot, after_command=self._sell_robot
        )
        self.invoker.register(
            "9", Commands.list_robots, after_command=self._list_robots
        )
        self.invoker.register("0", Commands.exit, after_command=None)

    # AfterCommands methods to update the state
    def _create_robot(self, robot: Robot):
        try:
            self.state.park_robot(robot)
            print(
                f"**** Robot {robot.name} ({robot.owner}) successfully created"
                f" ****"
            )
        except GarageFullException:
            print(
                "-> ERROR: Garage is full, create a bigger one or remove a "
                "robot"
            )
        except RobotAlreadyInException:
            print(
                f"-> ERROR: {robot.name} ({robot.owner} already exist in the "
                f"garage)"
            )

    def _create_garage(self, garage: Garage):
        self.state.update_garage(garage)
        print("**** Garage successfully created ****")

    def _list_robots(self, flag: bool):
        if flag:
            robots = self.state.get_robots()
        else:
            robots = []
        for i in range(1, len(robots)):
            print(f"{i}- {robots[i].name} ({robots[i].owner})")

    def _sell_robot(self, data):
        try:
            name, owner, buyer = data
            sale = self.state.remove_robot_from_garage(name, owner)
            sale.owner = buyer
            self.state.park_robot(sale)
            print(f"**** Operation Completed, {buyer} own to {name} now ****")
        except RobotNotFoundException:
            print(
                f"-> ERROR: The robot {name} ({owner}) does not exist in the "
                f"garage"
            )

    def _perform_action(self, data):
        try:
            name, owner, action = data
            robot = self.state.remove_robot_from_garage(name, owner)

            if action == "move":
                robot.move()
            if action == "work":
                robot.work()
            if action == "hibernate":
                robot.hibernate()
            if action == "talk":
                robot.talk()

            self.state.park_robot(robot)
            self.state.update_history((action, robot.name, robot.owner))
            print(
                f"**** {name} ({owner}) completed the action ({action}) "
                f"successfully ****"
            )

        except RobotNotFoundException:
            print(
                f"-> ERROR: The robot {name} ({owner}) does not exist in the "
                f"garage"
            )
        except UnhappyException:
            print(
                f"-> ERROR: {name} ({owner}) has no happiness to perform the "
                f"action"
            )
        except NoEnergyException:
            print(
                f"-> ERROR: {name} ({owner}) has no energy to perform the "
                f"action"
            )
        except RobotAlreadyInException:
            print(
                f"-> ERROR: {robot.name} ({robot.owner} already exist in the "
                f"garage)"
            )
        except GarageFullException:
            print(
                "-> ERROR: Garage is full, create a bigger one or remove a "
                "robot"
            )

    def _create_procedure(self, dict):
        proc_time = dict["proc_time"]
        candidates = dict["robots"]
        bots = [Robot]
        for i in candidates:
            name, owner = i
            try:
                bots.append(self.state.get_robot_info(name, owner))
            except RobotNotFoundException:
                print(
                    f"-> ERROR: The robot {name} ({owner}) does not exist, "
                    f"skipped"
                )
        self.state.procedures.append(Procedure(proc_time, bots))
        print("**** Procedure successfully created ****")

    def _apply_procedure(self, flag: bool):
        procs = [int]
        procedures = self.state.get_procedures()

        if flag:
            for i in range(1, len(procedures)):
                print(f"{i}- Time: {procedures[i].time}, "
                      f"Robots: {procedures[i].robots}")
        user_input = input("Add procedure to execute (y/n): ")
        while user_input != "n":
            try:
                id = int(input("Procedure number: "))
                if id < len(procedures) and id > 0:
                    procs.append(id)
                else:
                    print("-> ERROR: Procedure number is not allowed")
            except ValueError:
                print("-> ERROR: Procedure number is not allowed")
            user_input = input("Add procedure to execute (y/n): ")

        if len(procs) > 1:
            for i in procs:
                procedures[i-1].update_time()

    def _show_robot_info(self, data):
        name, owner = data
        try:
            robot = self.state.get_robot_info(name, owner)
            print(f"Robot name: {robot.name}")
            print(f"Owner: {robot.owner}")
            print(f"Energy: {robot.energy}")
            print(f"Happiness: {robot.happiness}")
            print(f"Procedure time: {robot.procedure_time}")
        except RobotNotFoundException:
            print(
                f"-> ERROR: The robot {name} ({owner}) does not exist in the "
                f"garage"
            )

    def _show_history(self, flag: bool):
        history = self.state.get_history()

        for i in history:
            print(f"- Action: {i[0]}, Robot: {i[1]} ({i[2]})")

    # Add some example data
    def populate_data(self):
        self.state.garage = Garage(3)

        # Create the robots
        r2d2 = Robot("R2D2", 20, 40, 0, "Anakin")
        c3po = Robot("C3PO", 30, 50, 0, "Vader")
        bb8 = Robot("BB8", 10, 45, 0, "Rei")

        # Park the robots
        self.state.garage.park_robot(r2d2)
        self.state.garage.park_robot(c3po)
        self.state.garage.park_robot(bb8)

        # Create procedures
        self.state.procedures = [
            Procedure(50, robots=[r2d2, bb8]),
            Procedure(60, robots=[r2d2, c3po]),
            Procedure(100, robots=[r2d2, c3po, bb8]),
            Procedure(150, robots=[bb8]),
            Procedure(200, robots=[r2d2])
        ]

    def run(self):
        # Execution loop
        Commands.start()
        c = input()

        while c != "0":
            print()
            try:
                self.invoker.execute(c)
            except CommandNotFoundException:
                print("-> ERROR: Command not found!!")

            Commands.start()
            c = input()

        # Exit command
        self.invoker.execute("0")
