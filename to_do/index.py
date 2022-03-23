# -*- coding: utf-8 -*-
__author__ = 'SirHades696'
__email__ = 'djnonasrm@gmail.com'

from flask import (
    Blueprint,
    render_template
)

from datetime import datetime

bp = Blueprint('index',__name__)

@bp.route('/')
def index():
    date = datetime.now()
    return render_template('index/index.html', date=date)