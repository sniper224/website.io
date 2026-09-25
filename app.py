from flask import Flask, render_template, request
usernames_passwords = {
    'user1': 'password1',
    'user2': 'password2',
    'user3': 'password3'
}

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    return render_template('login.xhtml')

@app.route('/login_val', methods=['POST'])
def login_val():
    name = request.form.get('username')
    password = request.form.get('password')
    if name in usernames_passwords and usernames_passwords[name] == password:
        return render_template('home.xhtml')  
    else:
        return render_template('login.xhtml')       
if __name__ == '__main__':
    app.run(debug=True)