"""The albumjet flask app viewss
"""

from flask import jsonify, render_template, request

from . import app, db
from .models import UserAlbum, UserLamina
from .functions import toBoolean


@app.route('/')
def index():
    """index view
    """
    
    useralbum = UserAlbum.query.get(1)
    return render_template('albumjet.html', useralbum=useralbum)


@app.route('/ajax/lamina/mark', methods=['GET', 'POST'])
def mark_lamina():
    """mark or unmark lamina
    """
    
    id = request.args.get('iduserlamina', 0)
    mark = toBoolean(request.args.get('mark', False))
    
    userlamina = UserLamina.query.get(id)
    userlamina.mark = mark
    db.session.commit()

    return jsonify(result="ok")
