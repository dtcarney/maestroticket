from flask import Blueprint, jsonify, abort, request
from ..models import Ticket, db, User,Concert

bp = Blueprint('concerts', __name__, url_prefix='/concerts')

@bp.route('', methods=['GET']) # decorator takes path and list of HTTP verbs
def index():
    concerts = Concert.query.all() # ORM performs SELECT query
    result = []
    for c in concerts:
        result.append(c.serialize()) # build list of concerts as dictionaries
    return jsonify(result) # return JSON response

@bp.route('/<int:id>', methods=['GET']) # decorator takes path and list of HTTP verbs
def show(id:int):
    concert = Concert.query.get_or_404(id)
    return jsonify(concert.serialize()) # return JSON response

