from app.application.queries import Query
from app.application.query_handlers import QueryResult
from app.domain.users.repositories import UserRepository
from app.domain.value_objects import UUID


class GetUserQuery(Query):
    user_id: UUID


# TODO: not imlemented yet
def get_user(query: GetUserQuery, repository: UserRepository) -> QueryResult:
    user = repository.get_by_id(id=query.user_id)
    if user:
        return
    return
