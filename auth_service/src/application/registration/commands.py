from app.application.commands import Command


class ChangePasswordCommand(Command):
    access_token: str
    old_password: str
    new_password: str
    new_password_repeated: str


class ConfirmUserRegistratioCommand(Command):
    confirmation_link: str


class RegisterNewUserCommand(Command):
    first_name: str
    last_name: str
    email: str
    password: str


class SendRegistrationConfirmationEmailCommand(Command):
    email: str
    confirmation_link: str
    confirmation_code: str
