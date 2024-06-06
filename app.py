from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        number1 = int(request.form['number1'])
        number2 = int(request.form['number2'])
        result = number1 + number2
        return jsonify({'result': result})
    except ValueError:
        return jsonify({'error': 'Invalid input. Please enter integer numbers only.'})

if __name__ == '__main__':
    app.run(debug=True)