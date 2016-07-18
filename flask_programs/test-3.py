from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
@app.route('/result')

def index():
    dict={'telugu': 95,'hindi':86, 'english':85 ,'maths':100, 'science':95,'social':96}
    return render_template("3.html",title='Home',result=dict)

if __name__ == '__main__':
    app.run(debug=True)
