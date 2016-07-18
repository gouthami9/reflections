from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def student():
    return render_template('add.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form['message'] + ' ' + request.form['name'] + ' ' + request.form['surname']
        return render_template('add1.html', string=result)


if __name__ == '__main__':
    app.run(debug=True)
