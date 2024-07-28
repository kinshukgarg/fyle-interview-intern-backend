from flask import Blueprint, request, jsonify
from core import db
from core.apis.decorators import authenticate_principal, accept_payload
from core.models.assignments import Assignment, AssignmentStateEnum, GradeEnum
from core.models.teachers import Teacher
from core.schema import AssignmentSchema, AssignmentGradeSchema

principal_resources = Blueprint('principal_resources', __name__)

@principal_resources.route('/principal/teachers', methods=['GET'])
@authenticate_principal
def get_all_teachers(p):
    teachers = Teacher.query.all()
    return jsonify({'data': [teacher.to_dict() for teacher in teachers]}), 200

@principal_resources.route('/principal/assignments', methods=['GET'])
@authenticate_principal
def get_all_assignments(p):
    assignments = Assignment.query.filter(Assignment.state.in_([AssignmentStateEnum.SUBMITTED, AssignmentStateEnum.GRADED])).all()
    return jsonify({'data': [assignment.to_dict() for assignment in assignments]}), 200

@principal_resources.route('/principal/assignments/grade', methods=['POST'])
@authenticate_principal
@accept_payload
def grade_assignment_as_principal(p, incoming_payload):
    data = incoming_payload
    assignment = Assignment.query.get(data['id'])
    if not assignment:
        return jsonify({'error': 'Assignment not found'}), 404
    if assignment.state == AssignmentStateEnum.DRAFT:
        return jsonify({'error': 'Cannot grade a draft assignment'}), 400

    assignment.grade = data['grade']
    assignment.state = AssignmentStateEnum.GRADED
    db.session.commit()
    return jsonify({'data': assignment.to_dict()}), 200
