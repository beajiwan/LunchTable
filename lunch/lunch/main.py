from flask import Flask, render_template, redirect, url_for, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('table'))

@app.route('/table', methods=['GET'])
def table():
    return render_template('table.html', win_result=get_sample_win_result())

def get_sample_win_result():
    return {
        'win result': {}
    }

@app.route('/save_checkbox_state', methods=['POST'])
def save_checkbox_state():
    data = request.get_json()
    checkbox_id = data.get('checkboxId')
    is_checked = data.get('isChecked')

    local_path = r'C:\Lunchpath'
    file_path = os.path.join(local_path, f'{checkbox_id}.txt')

    with open(file_path, 'w') as file:
        file.write(str(is_checked))

    return jsonify({'status': 'success'})

@app.route('/get_checkbox_state/<checkbox_id>', methods=['GET'])
def get_checkbox_state(checkbox_id):
    local_path = r'C:\Lunchpath'
    file_path = os.path.join(local_path, f'{checkbox_id}.txt')

    try:
        with open(file_path, 'r') as file:
            # 파일에서 체크박스 상태를 읽어와 반환
            return jsonify({'isChecked': bool(file.read().strip())})
    except FileNotFoundError:
        # 파일이 없는 경우 False 반환
        return jsonify({'isChecked': False})


if __name__ == '__main__':
    app.run(debug=True)