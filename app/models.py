from typing import List
import sqlalchemy as sa
import sqlalchemy.orm as so

from app import db


class RBFB(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    topic: so.Mapped[str] = so.mapped_column(sa.String(64), index=True)
    candidates: so.WriteOnlyMapped["Candidate"] = so.relationship(back_populates="parent")
    urlval: so.Mapped[str] = so.mapped_column(sa.String(8))
    def __repr__(self):
        return f'<RBFB {self.topic}>'


class Candidate(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    parent_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(RBFB.id))
    parent: so.Mapped[RBFB] = so.relationship(back_populates="candidates")
    value: so.Mapped[str] = so.mapped_column(sa.String(64))
    real: so.Mapped[bool] = so.mapped_column(sa.Boolean())

    def __repr__(self):
        return f'<{self.parent.topic}>: {self.value}, real={self.real}'

