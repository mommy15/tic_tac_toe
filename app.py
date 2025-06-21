from flask import Flask, render_template, request, jsonify
from ai import find_best_move, is_winner, is_board_full

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/move', methods=['POST'])
def move():
    data = request.json
    board = data['board']
    best_move = find_best_move(board)
    return jsonify({'row': best_move[0], 'col': best_move[1]})

if __name__ == '__main__':
    app.run(debug=True)
