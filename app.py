from flask import Flask,render_template

app = Flask(__name__)

# @app.route('/')
# def index():
#     return 'Hello world'
# @app.route('/whereami')
# def whereami():
#     return 'Ghana!'

# @app.route("/user/<name>")
# def welcome(name):
#     return f"Welcome,{ (name)}!"

@app.route('/')
def index():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')