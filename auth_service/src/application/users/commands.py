from app.application.commands import Command
from app.application.command_handlers import CommandResult
from app.domain.users.repositories import UserRepository
from app.domain.users.entities import User
from app.domain.value_objects import UUID


class ChangeUserDetailsCommand(Command):
    user_id: UUID
    first_name: str
    last_name: str


# TODO: implement command handler
# @command_handler
def change_user_details(
    command: ChangeUserDetailsCommand, repository: UserRepository
) -> CommandResult:
    user: User = repository.get_by_id(command.user_id)
    events = user.update_datails(first_name=command.first_name, last_name=command.last_name)
    repository.update(user)

    return CommandResult.ok(events=events)
