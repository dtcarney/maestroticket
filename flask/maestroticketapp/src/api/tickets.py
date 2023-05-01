from flask import Blueprint, jsonify, abort, request
from ..models import Ticket, db, User

bp = Blueprint('tickets', __name__, url_prefix='/tickets')

@bp.route('', methods=['GET']) # decorator takes path and list of HTTP verbs
def index():
    tickets = Ticket.query.all() # ORM performs SELECT query
    result = []
    for t in tickets:
        result.append(t.serialize()) # build list of tickets as dictionaries
    return jsonify(result) # return JSON response


@bp.route('', methods=['POST'])
def create():
    # req body must contain user_id and content
    if 'user_id' not in request.json or 'concert_id' not in request.json:
        return abort(400)
    # user with id of user_id must exist
    User.query.get_or_404(request.json['user_id'])
    # construct Ticket
    t = Ticket(
        user_id=request.json['user_id'],
        concert_id=request.json['concert_id'],
        tickets_purchased=request.json['tickets_purchased']
    )
    db.session.add(t) # prepare CREATE statement
    db.session.commit() # execute CREATE statement
    return jsonify(t.serialize())