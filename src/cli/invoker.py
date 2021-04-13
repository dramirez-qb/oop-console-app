from collections.abc import Callable


class CommandNotFoundException(Exception):
    pass


class Invoker:
    # The Invoker Class
    def __init__(self):
        self._commands = {}
        self._after_commands = {}

    def register(
        self,
        command_code: str,
        command: Callable,
        after_command: Callable,
    ):
        #  Register commands in the Invoker
        self._commands[command_code] = command
        self._after_commands[command_code] = after_command

    def execute(self, command_code):
        # Execute any registered commands
        if command_code not in self._commands.keys():
            raise CommandNotFoundException()

        # Execute command
        response = self._commands[command_code]()

        # Execute after command function
        after_command = self._after_commands[command_code]
        if after_command and response:
            after_command(response)
