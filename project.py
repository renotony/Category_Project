from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Plays, Characters, User
from flask import session as login_session
import random, string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Tony's Plays"



engine = create_engine('sqlite:///plays.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    # return "The current session state is %s" % login_session['state']
    return render_template('login.html', STATE=state)

@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output


def getUserID(email):
    try:
        user = session.query(User).filter_by(email = email).one()
        return user.id
    except:
        return None

def getUserInfo(user_id):
    user = session.query(User).filter_by(id = user_id).one()
    return user

def createUser(login_session):
    newUser = User(name = login_session['username'], email = login_session['email'], picture = login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email = login_session['email']).one()
    return user.id

@app.route('/gdisconnect')
def gdisconnect():
        # Only disconnect a connected user.
    access_token = login_session.get('access_token')
    print("access_token = " + access_token)
    if access_token is None:
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]

    if result['status'] == '200':
        # Reset the user's sesson.
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']

        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        # For whatever reason, the given token was invalid.
        response = make_response(
            json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response

@app.route('/plays/JSON')
def playsJSON():
    plays = session.query(Plays).all()
    return jsonify(Plays=[i.serialize for i in plays])

@app.route('/plays/<int:play_id>/JSON')
@app.route('/plays/<int:play_id>/chars/JSON')
def playCharsJSON(play_id):
    play = session.query(Plays).filter_by(id=play_id).one()
    chars = session.query(Characters).filter_by(play_id=play_id).all()
    return jsonify(Chars=[i.serialize for i in chars])

@app.route('/plays/<int:play_id>/chars/<int:char_id>/JSON/')
def charJSON(play_id, char_id):
    char = session.query(Characters).filter_by(id=char_id).one()
    return jsonify(Char = char.serialize)

@app.route('/')
@app.route('/plays/')
def plays():
    titles = session.query(Plays).order_by(asc(Plays.title))
    if 'username' not in login_session:
        return render_template('publicplays.html', plays=titles)
    else:
        return render_template('plays.html', titles=titles)

@app.route('/plays/new', methods=['GET', 'POST'])
def newPlay():
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        newPlay = Plays(title = request.form['title'], user_id=login_session['user_id'])
        session.add(newPlay)
        session.commit()
        flash("new Play created!")
        return redirect(url_for('plays'))
    else:
        return render_template('newPlay.html')

@app.route('/plays/<int:play_id>/edit', methods=['GET', 'POST'])
def editPlay(play_id):
    if 'username' not in login_session:
        return redirect('/login')
    editedPlay = session.query(Plays).filter_by(id=play_id).one()
    if request.method == 'POST':
        if request.form['title']:
            editedPlay.title = request.form['title']
        session.add(editedPlay)
        session.commit()
        flash("Play name has been edited")
        return redirect(url_for('plays'))
    else:
        return render_template('editPlay.html', play_id = play_id, i = editedPlay)

@app.route('/plays/<int:play_id>/delete', methods=['GET', 'POST'])
def deletePlay(play_id):
    if 'username' not in login_session:
        return redirect('/login')
    deletedPlay = session.query(Plays).filter_by(id=play_id).one()
    if request.method == 'POST':
        session.delete(deletedPlay)
        session.commit()
        flash("Play has been deleted")
        return redirect(url_for('plays'))
    else:
        return render_template('deletePlay.html', i = deletedPlay)


@app.route('/plays/<int:play_id>/')
@app.route('/plays/<int:play_id>/chars')
def playChars(play_id):
    play = session.query(Plays).filter_by(id = play_id).one()
    characters = session.query(Characters).filter_by(play_id = play.id).all()
    return render_template('chars.html', play=play, characters=characters)

@app.route('/plays/<int:play_id>/new', methods=['GET', 'POST'])
def newCharacter(play_id):
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        newChar = Characters(name = request.form['name'], description=request.form['description'], play_id = play_id, user_id=login_session['user_id'])
        session.add(newChar)
        session.commit()
        flash("new character created!")
        return redirect(url_for('playChars', play_id=play_id))
    else:
        return render_template('newChar.html', play_id=play_id)

@app.route('/plays/<int:play_id>/<int:char_id>/edit', methods=['GET', 'POST'])
def editCharacter(play_id, char_id):
    if 'username' not in login_session:
        return redirect('/login')
    editedChar = session.query(Characters).filter_by(id = char_id).one()
    playList = session.query(Plays).all()
    if request.method == 'POST':
        if request.form['name']:
            editedChar.name = request.form['name']
        if request.form['description']:
            editedChar.description = request.form['description']
        if request.form['playlist']:
            editedChar.play_id = request.form['playlist']
        session.add(editedChar)
        session.commit()
        flash("Character has been edited")
        return redirect(url_for('playChars', play_id = play_id))
    else:
        return render_template('editChar.html', play_id = play_id, char_id = char_id, i = editedChar, option_list = playList)

@app.route('/plays/<int:play_id>/<int:char_id>/delete', methods=['GET', 'POST'])
def deleteCharacter(play_id, char_id):
    if 'username' not in login_session:
        return redirect('/login')
    charToDelete = session.query(Characters).filter_by(id=char_id).one()
    if request.method == 'POST':
        session.delete(charToDelete)
        session.commit()
        flash("Character has been deleted")
        return redirect(url_for('playChars', play_id = play_id))
    else:
        return render_template('deleteChar.html', i = charToDelete)

@app.route('/plays/<int:play_id>/<int:char_id>/description')
def charDesc(play_id, char_id):
    play = session.query(Plays).filter_by(id = play_id).one()
    character = session.query(Characters).filter_by(id = char_id).one()
    return render_template('charDesc.html', play=play, character=character)

@app.route('/plays/<int:play_id>/<int:char_id>/cleardesc', methods=['GET', 'POST'])
def clearDesc(play_id, char_id):
    if 'username' not in login_session:
        return redirect('/login')
    editedChar = session.query(Characters).filter_by(id = char_id).one()
    playList = session.query(Plays).all()
    if request.method == 'POST':
            editedChar.description = ""
            session.add(editedChar)
            session.commit()
            flash("Description has been deleted")
            return redirect(url_for('playChars', play_id = play_id))
    else:
            return render_template('deleteDesc.html', play_id = play_id, char_id = char_id, i = editedChar)



if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
