from flask import Blueprint, jsonify, abort, request
from sqlalchemy import func
from ..models import Ticket, db, User,Concert

bp = Blueprint('concert_tickets_sold', __name__, url_prefix='/concert_tickets_sold')



@bp.route('/<int:id>', methods=['GET']) # decorator takes path and list of HTTP verbs
def show(id:int):
    concert = Concert.query.get_or_404(id)
    tickets_sold = Ticket.query.filter_by(concert_id=id).with_entities(func.sum(Ticket.tickets_purchased)).scalar()
    return jsonify({'tickets_sold': tickets_sold})

