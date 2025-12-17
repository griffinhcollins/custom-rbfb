import sqlalchemy as sa
import sqlalchemy.orm as so
from app import app, db
from app.models import RBFB, Candidate

@app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'so': so, 'db': db, 'RBFB': RBFB, 'Candidate': Candidate}