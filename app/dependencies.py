from typing import Annotated

from sqlalchemy.orm import Session
from fastapi import Depends

from app.database import get_db

db_dependency=Annotated[Session, Depends(get_db)]

