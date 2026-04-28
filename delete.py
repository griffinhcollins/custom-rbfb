from app import db, app
from app.models import RBFB, Candidate
import sqlalchemy as sa


with app.app_context():
    # Find the row you want to delete
    rbfb = db.session.scalars(sa.select(RBFB).where(RBFB.topic == "<insert topic here>")).all()
    print(rbfb)

    ids = [r.id for r in rbfb]
    db.session.execute(sa.delete(Candidate).where(Candidate.parent_id.in_(ids)))
    db.session.execute(sa.delete(RBFB).where(RBFB.id.in_(ids)))
    db.session.commit()