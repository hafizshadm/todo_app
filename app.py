# Application Is Powered by FLASK (Python)
from flask import Flask, render_template, request, redirect, url_for, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
import sys


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/todo_app'
db = SQLAlchemy(app)

class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)
    def __repr__(self):
        return f'<Todo {self.id} {self.description}>'


@app.route('/todos/<todo_id>/set-completed', methods=['POST'])
def update_todo(todo_id):
    try:
        completed = request.get_json()['completed']
        todo = Todo.query.get(todo_id)
        todo.completed = completed
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()
        return redirect(url_for('index'))

@app.route('/todos/create', methods=['POST'])
def create_todo():
    error = False
    body = {}
    try:
        # description = request.form.get('description', '')
        description = request.get_json()['description']
        todo = Todo(description=description)
        db.session.add(todo)
        db.session.commit()
        # return redirect(url_for('index'))
        # return render_template('index.html', data=Todo.query.all())
        body['description'] = todo.description
    except:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        abort(400)
    else:
        return jsonify(body)
        # return render_template('index.html', data=Todo.query.order_by('id').all())

@app.route('/')
def index():
    db.create_all()
    return render_template('index.html', data=Todo.query.order_by('id').all())


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5000)