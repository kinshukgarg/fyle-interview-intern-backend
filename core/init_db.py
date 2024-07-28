import sys
import os

# Add the project root directory to the system path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/fyle-interview-intern-backend')

from core import db
from core.server import app
from core.models.assignments import Assignment
from core.models.principals import Principal
from core.models.students import Student
from core.models.teachers import Teacher
from core.models.users import User

with app.app_context():
    db.create_all()
