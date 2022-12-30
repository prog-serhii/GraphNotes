from app.application.commands import Command
from app.domain.session.services import SessionAuthenticationService


class EmailLoginCommand(Command):
    remember_me: bool
    user_agent: str
    ip_address: str
    email: str
    password: str


class LogoutCommand(Command):
    auth_token: str


class SessionAuthenticationCommand(Command):
    auth_token: str


def login():
    pass


def logout(command: LogoutCommand, session_auth_service: SessionAuthenticationService):
    session_auth_service.logout(command.auth_token)


def authenticate(command: SessionAuthenticationCommand, session_auth_service: SessionAuthenticationService):
    session_auth_service.authenticate(command.auth_token)
