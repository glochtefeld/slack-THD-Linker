import os
from dotenv import load_dotenv
import re
from flask import abort, Flask, jsonify, request, redirect, render_template
from slackclient import SlackClient

# initialize dotenv
dotenv_path = os.path.join(os.path.dirname(__file__),'.env')
load_dotenv(dotenv_path)


app = Flask(__name__)

# Variables
# APPLICATION_TOKEN
# CLIENT_ID
# CLIENT_SECRET

# Checks token from request against app_token
def is_request_valid(request):
    is_token_valid = False
    if request.form['token'] == os.environ['APPLICATION_TOKEN']:
        is_token_valid = True
    return is_token_valid

# Main parser. Takes str input, uses regex to find if word contains ticket #.
def parse(txt):
    # if the only text is help, will return a string.
    if txt == "help":
        build_str = "This will return a completed link to that ticket in KBOX. Neat, huh?"
        return build_str
    txt = txt.split()
    build_str = ""
    for word in txt:
        if re.search(".*\d{5,7}",word):
            build_str = "<https://help.luther.edu/adminui/ticket.php?ID=" + word + '>'
            return build_str

###############
## Web pages ##
###############
@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/')
def index():
    return render_template('index.html',cli_id = os.environ['CLIENT_ID'])

@app.route('/support')
def support():
    return render_template('support.html')

# Slash command, needs POST method
@app.route('/ticket', methods=['POST'])
def hello_there():
    # Checks validity of request
    if not is_request_valid(request):
        abort(400)
    text = request.form.get('text')
    res_text = parse(text)
    # Returned link is pasted into the channel.
    return jsonify({'response_type':'in_channel','text':res_text})

# Redirection to slack Oauth
@app.route('/authorize')
def redir():
    return redirect('https://slack.com/oauth/authorize?client_id='+ os.environ['CLIENT_ID']+'&scope=commands', code=302)

# Callback URL; returns whether or not app was successfully added. 
@app.route('/oauth/authorized', methods=['GET', 'POST'])
def called_back():
    a_code = request.args['code']
    sc = SlackClient("")

    auth_response = sc.api_call(
                                "oauth.access",
                                client_id = os.environ['CLIENT_ID'],
                                client_secret = os.environ['CLIENT_SECRET'],
                                code=a_code)

    os.environ["SLACK_USER_TOKEN"] = auth_response['access_token']
    #os.environ["SLACK_BOT_TOKEN"] = auth_response['bot']['bot_access-token']
    return 'Auth completed.'


if __name__ == '__main__':
    app.run(debug=True,port=5001)
