from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/table', methods = ['GET'])
def table():
    return render_template('table.html',win_result=get_sample_win_result())


def get_sample_win_result():
    # 여기에 실제로 사용할 데이터를 가져오는 코드를 추가하세요.
    # 임시로 예제 데이터를 반환하도록 설정했습니다.
    return {
        'round': 123,
        'win result': {
            'numbers': [1, 2, 3, 4, 5, 6],
            'bonus': 7,
            'win': {'rank1': {'total': 10, 'num': 5}, 'rank2': {'total': 5, 'num': 3}}
        }
    }

if __name__=='__main__':
    app.run()