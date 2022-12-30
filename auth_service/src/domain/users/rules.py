from auth_service.app.domain.rules import BusinessRule
from auth_service.app.domain.users.repositories import UserRepository


class UserEmailMustBeUnique(BusinessRule):
    ___message = 'User with this email already exists.'

    user_repository: UserRepository
    email: str

    def is_broken(self) -> bool:
        return bool(self.user_repository.find_by_email(self.email))
