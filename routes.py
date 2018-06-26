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


def is_request_valid(request):
    is_token_valid = False

    if request.form['token'] == os.environ['APPLICATION_TOKEN']:
        is_token_valid = True


    return is_token_valid

def parse(txt):
    if txt == "help":
        buildStr = "This will return a completed link to that ticket in KBOX. Neat, huh?"
        return buildStr

    txt = txt.split()
    buildStr = ""

    for word in txt:
        if re.search(".*\d{5,7}",word):
            buildStr = "<https://help.luther.edu/adminui/ticket.php?ID=" + word + '>'
            return buildStr

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/')
def index():
    return render_template('index.html',cli_id = os.environ['CLIENT_ID'])

@app.route('/support')
def support():
    return render_template('support.html')


@app.route('/ticket', methods=['POST'])
def hello_there():
    if not is_request_valid(request):
        abort(400)
    text = request.form.get('text')
    resText = parse(text)

    return jsonify({'response_type':'in_channel','text':resText})

@app.route('/authorize')
def redir():
    return redirect('https://slack.com/oauth/authorize?client_id='+ os.environ['CLIENT_ID']+'&scope=commands', code=302)

@app.route('/oauth/authorized', methods=['GET', 'POST'])
def calledBack():
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
