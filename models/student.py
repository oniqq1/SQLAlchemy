from __future__ import annotations

from typing import (List, Optional)

from sqlalchemy.orm import (Mapped, mapped_column, relationship)

from . import Base

from sqlalchemy import String

from .group import Group

from .associates import student_group_assoc_table



class Student(Base):
    __tablename__ = "student"


    def __repr__(self):
        return      (f"student name = {self.name} \n"
                     f"student surname = {self.surname} \n"
                     f"student id = {self.id} \n")

    id: Mapped[int] = mapped_column(primary_key=True)
    surname: Mapped[Optional[str]]
    name: Mapped[str] = mapped_column(String(50))
    age: Mapped[int] = mapped_column()
    address: Mapped[str] =mapped_column(String(250))

    groups: Mapped[List[Group]] = relationship(
        secondary=student_group_assoc_table
    )