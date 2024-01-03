from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/app.db'
db = SQLAlchemy(app)

class CheckboxState(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    checkbox_id = db.Column(db.String(50), nullable=False)
    is_checked = db.Column(db.Boolean, default=False)

@app.route('/')
def index():
    return redirect(url_for('table'))

@app.route('/table', methods=['GET'])
def table():
    checkbox_states = CheckboxState.query.all()
    return render_template('table.html', checkbox_states=checkbox_states)

@app.route('/save_checkbox_state', methods=['POST'])
def save_checkbox_state():
    data = request.get_json()
    checkbox_id = data.get('checkboxId')
    is_checked = data.get('isChecked')

    checkbox_state = CheckboxState.query.filter_by(checkbox_id=checkbox_id).first()

    if checkbox_state is None:
        checkbox_state = CheckboxState(checkbox_id=checkbox_id)

    checkbox_state.is_checked = is_checked
    db.session.add(checkbox_state)
    db.session.commit()

    return jsonify({'status': 'success'})

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)