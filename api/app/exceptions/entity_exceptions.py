from fastapi.exceptions import HTTPException


class EntityAlreadyRegisteredException(HTTPException):
    def __init__(self, entity_name: str):
        super().__init__(
            status_code=400,
            detail=f'{entity_name} already registered.'
        )


class EntityNotFoundException(HTTPException):
    def __init__(self, entity_name: str, entity_id: int):
        super().__init__(
            status_code=404,
            detail=f'{entity_name} with id {entity_id} not found.'
        )
