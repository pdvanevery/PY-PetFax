from flask import (Blueprint, render_template)
import json

pets = json.load(open('pets.json'))
print(pets)

bp = Blueprint('pet', __name__, url_prefix='/pets')

@bp.route('/')
def index():
    return render_template('index.html', pets=pets)
    
@bp.route('/show')
def show():
    return render_template('show.html', pets=pets)

