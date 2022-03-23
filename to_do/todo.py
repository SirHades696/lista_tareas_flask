# -*- coding: utf-8 -*-
__author__ = 'SirHades696'
__email__ = 'djnonasrm@gmail.com'

from flask import (
    Blueprint, 
    flash,
    g,
    redirect, 
    render_template,
    request,
    url_for
)
from werkzeug.exceptions import abort
from to_do.auth import login_required
from to_do.db import get_db

bp = Blueprint('todo', __name__)

@bp.route('/list')
@login_required
def list():
    db, c = get_db()
    c.execute(
        """Select 
        todo.id, todo.description, user.username,
        todo.complete, todo.created_at  
        from todo, user where todo.created_by = user.id and todo.created_by=%s order by todo.created_at DESC""",(g.user['id'],)
    )
    todos = c.fetchall()
    return render_template('todo/list.html', todos=todos)

@bp.route('/create',methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        description = request.form['description']
        error = None
        if not description:
            error = 'Descripción requerida'
            
        if error is not None:
            flash(error)
        else:
            db, c = get_db()
            c.execute(
                'Insert into todo (description, complete, created_by)'
                ' values (%s,%s,%s)',(description,False,g.user['id'])
            )
            db.commit()
            return redirect(url_for('todo.list'))
        
    return render_template('todo/create.html')

def get_todo(id):
    db,c = get_db()
    c.execute(
        """select 
        todo.id, todo.description, todo.complete, todo.created_by,
        todo.created_at, user.username
        from todo,user where todo.created_by=user.id and todo.id = %s""",(id,)
    )
    todo = c.fetchone()
    if todo is None:
        abort(404, 'El todo de id {0} no existe'.format(id))
    return todo

@bp.route('/<int:id>/update',methods=['GET', 'POST'])
@login_required
def update(id):
    todo = get_todo(id)
    if request.method == 'POST':
        description = request.form['description']
        complete = True if request.form.get("complete") == 'on' else False
        error = None
        if not description:
            error = "Descripción requerida"
        if error is not None:
            flash(error)
        
        else:
            db, c = get_db()
            c.execute(
                """update todo set description = %s , complete = %s where 
                id = %s and created_by=%s""", (description, complete, id, g.user['id'])
            )
            db.commit()
            return redirect(url_for('todo.list'))
        
    return render_template('todo/update.html',todo=todo)

@bp.route('/<int:id>/delete',methods=['POST'])
@login_required
def delete(id):
    db,c = get_db()
    c.execute(
        'delete from todo where id=%s and created_by = %s', (id, g.user['id'])
    )
    db.commit()
    return redirect(url_for('todo.list'))