from typing import Any, List, Mapping, Optional

from src.core.command import Command


class Application:
    def __init__(
        self,
        commands: Optional[List[Command]] = None,
        root_args: Optional[List[Command.Argument]] = None,
    ) -> None:
        self.commands = commands or []
        self.root_args = root_args or []

        self._command_mapping: Mapping[str, Command] = {}
        for command in self.commands:
            self._command_mapping[command.name] = command

    async def run(self, args: Any):
        command = self._command_mapping[args.command]
        await command.run(args)
