from app.domain.entities import Entity
from app.domain.value_objects import UUID
# from auth_service.app.domain.users.rules import UserEmailMustBeUnique
# from app.domain.users.events import UserCreated, UserNameChanged


class User(Entity):

    def __init__(self, user_id: UUID, first_name: str, last_name: str, email: str):
        super().__init__(user_id)
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    # TODO: later
    # def __post_init__(self) -> None:
        # self.check_rule(UserEmailMustBeUnique(user_repository='', email=self.email))
        # UserCreated

    # def update_datails(self, first_name: str, last_name: str) -> None:
    #     self.first_name = first_name
    #     self.last_name = last_name
    #     self._record_event(UserNameChanged(
    #         first_name=first_name,
    #         last_name=last_name,
    #         email=self.email
    #     ))
