from flask import Flask
from core.apis.responses import APIResponse

app = Flask(__name__)
app.response_class = APIResponse

from core.models import assignments, principals, students, teachers, users
from core.schema import AssignmentSchema, AssignmentSubmitSchema, AssignmentGradeSchema

from .student import student_assignments_resources
from .teacher import teacher_assignments_resources
from .principal import principal_resources

app.register_blueprint(student_assignments_resources)
app.register_blueprint(teacher_assignments_resources)
app.register_blueprint(principal_resources)
