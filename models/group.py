from sqlalchemy import String

from sqlalchemy.orm import (Mapped , mapped_column)

from . import Base


class Group(Base):
    __tablename__ = "group"

    def __repr__(self):
        return (f"student id = {self.id} \n"
                f"student name = {self.name} \n")


    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))