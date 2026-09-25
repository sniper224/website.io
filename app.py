from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('navigation.xhtml',store_name='M&S')

if __name__ == '__main__':
    app.run(debug=True)