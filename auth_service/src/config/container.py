from dependency_injector import containers, providers

from config.api_config import ApiConfig


class Container(containers.DeclarativeContainer):
    """Dependency Injection Container"""

    __self__ = providers.Self()

    config = providers.Configuration(pydantic_settings=[ApiConfig()])
