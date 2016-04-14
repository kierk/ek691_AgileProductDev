from flask import Flask, Response, render_template, redirect, url_for, request, session, abort
#from energenie import switch_on, switch_off
import subprocess
from flask.ext.login import LoginManager, UserMixin, login_required, login_user, logout_user

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

#---------------------------------------------------------
#  Login Classes
#---------------------------------------------------------

class User(UserMixin):
    # proxy for a database of users
#    user_database = {"root": ("root", "root"),
#               "JaneDoe": ("JaneDoe", "Jane")}

#    def __init__(self, username, password):
#        self.id = username
#        self.password = password

#    @classmethod
#    def get(cls,id):
#        return cls.user_database.get(id)
    def __init__(self, id):
        self.id = id
        self.name = "user" + str(id)
        self.password = self.name + '1'
        
    def __repr__(self):
        return "%d/%s/%s" % (self.id, self.name, self.password)


# create some users with ids 1 to 20       
users = [User(id) for id in range(1, 21)]





# somewhere to logout
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return Response('''
	<!doctype html>
	<html>
	<head>
	<title>DoorHub Logout Success :)</title>
	<link rel="stylesheet" href="/static/style.css" />
	</head>
	<body>
	<hr>
	<a>Logged Out :)</a>
	<hr>
	<a href="/">Home</a>
	<hr>
	</body>
	</html>
	''')


# handle login failed
@app.errorhandler(401)
def page_not_found(e):
    return Response('<p>Login failed</p>')
    
    
# callback to reload the user object        
@login_manager.user_loader
def load_user(userid):
    return User(userid)

comment1 = '''
@login_manager.request_loader
def load_user(request):
    token = request.headers.get('Authorization')
    if token is None:
        token = request.args.get('token')

    if token is not None:
        username,password = token.split(":") # naive token
        user_entry = User.get(username)
        if (user_entry is not None):
            user = User(user_entry[0],user_entry[1])
            if (user.password == password):
                return user
    return None
'''

#---------------------------------------------------------
#  Routing
#---------------------------------------------------------

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']        
        if password == username + '1':
            id = username
            user = User(id)
            login_user(user)
            return redirect(url_for('index'))
        else:
	    return Response('''
        	<h1>DoorHub Login</h1>
        	<form action="" method="post">
            	    <p><input type=text name=username>
            	    <p><input type=password name=password>
            	    <p><input type=submit value=Login>
        	</form>
            ''')

	    #print "AHHHHHHHHHHHH..\n\n"
            #return abort(401)
    else:
        return Response('''
	<h1>DoorHub Login</h1>
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=password name=password>
            <p><input type=submit value=Login>
        </form>
        ''')


#@app.route('/login', methods=['GET', 'POST'])
#def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
#    form = LoginForm()
#    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class
#        login_user(user)

#        flask.flash('Logged in successfully.')

#        next = flask.request.args.get('next')
        # next_is_valid should check if the user has valid
        # permission to access the `next` url
#        if not next_is_valid(next):
#            return flask.abort(400)

#        return flask.redirect(next or flask.url_for('index'))
#    return flask.render_template('login.html', form=form)


@app.route('/',methods=["GET"])
@login_required
def index():
    return render_template('index.html')


@app.route('/seclog/',methods=["GET"])
def seclog():
    with open( 'doorhub.log','r') as f:
	content = f.read()
    return render_template('template.html', content=content)

@app.route('/cVepr0rR37821as12lk3/',methods=["GET"])
def unauth():
    return render_template('index2.html')

@app.route('/unon/')
def unon():
    print "Opening Door From Un-Authenticated"
    # Uncomment to run Script
    # subprocess.Popen(['/usr/bin/env', 'python', 'open.py'], subprocess.PIPE)
    #app.r('/off/')
    return redirect(url_for('unauth'))



@app.route('/on/')
def on():
    print "Opening Door From Authenticated"
    # Uncomment to run Script
    # subprocess.Popen(['/usr/bin/env', 'python', 'open.py'], subprocess.PIPE)
    #app.r('/off/')
    return redirect(url_for('index'))


@app.route('/onepass/', methods=["GET", "POST"])
def onepass():
    # print "Texting Onetime Pass"
    # Uncomment to run Script
    # subprocess.Popen(['/usr/bin/env', 'python', 'onepass.py'], subprocess.PIPE)
    # app.r('/off/')
#    return redirect(url_for('index'))
    if request.method == 'POST':
        pnumber = request.form['pnumber']
        hours = request.form['hours']
        if pnumber:
	    if hours:
	        print "HEY LMAO IT WORKED JALELUIA"

		subprocess.Popen(['/usr/bin/env', 'python', 'onepass.py', pnumber, hours], subprocess.PIPE)
		return redirect(url_for('index'))
        #    id = username
        #    user = User(id)
        #    login_user(user)
        #    return redirect(url_for('index'))
        else:
            return Response('''
                <h1>Please Fill Out Both Forms:</h1>
                <form action="" method="post">
		    Phone Number:<br>
                    <p><input type=text name=pnumber>
		    Hours:<br>
                    <p><input type=text name=hours>
                    <p><input type=submit value=OneTime>
                </form>
            ''')

            #print "AHHHHHHHHHHHH..\n\n"
            #return abort(401)
    else:
        return Response('''
        <h1>OneTime Pass:</h1>
        <form action="" method="post">
	    Phone Number:<br>
            <p><input type=text name=pnumber><br>
	    Hours:<br>
            <p><input type=text name=hours>
            <p><input type=submit value=OneTime>
        </form>
        ''')



@app.route('/off/')
def off():
    #switch_off()
    return render_template('index.html')

if __name__ == '__main__':
    app.config["SECRET_KEY"] = "ITSASECRET"
    app.run(debug=True, host='0.0.0.0', port=80)
