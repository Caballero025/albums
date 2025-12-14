from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Albums


alb_bp = Blueprint ('albums',__name__)



@alb_bp.route('/')
def index():
    albums = Albums.query.all()
    return render_template('index.html', albums = albums)

