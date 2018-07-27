import os
from dotenv import load_dotenv
import re
from flask import abort, Flask, jsonify, request, redirect, render_template
from slackclient import SlackClient
from survey_proc import post_survey
from slack_parse import parse


# initialize dotenv
dotenv_path = os.path.join(os.path.dirname(__file__),'.env')
load_dotenv(dotenv_path)


# initialize flask website
app = Flask(__name__)

def is_request_valid(request):
    is_token_valid = False
    if request.form['token'] == os.environ['APPLICATION_TOKEN']:
        is_token_valid = True
    return is_token_valid

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/')
def index():
    return render_template('index.html',text=GLOBAL_VARIABLE)

@app.route('/support')
def support():
    return render_template('support.html')

@app.route('/ticket', methods=['POST'])
def hello_there():
    if not is_request_valid(request):
        abort(400)
    text = request.form.get('text')
    (resText,res_types) = parse(text)
    return jsonify({'response_type':res_types,'text':resText})

@app.route('/survey', methods=['GET','POST'])
def survey():
    new_json = request.get_json('subject','body','')
    post_survey(new_json)
    return True

@app.route('/ticket/authorize')
def tick_redir():
    return redirect('https://slack.com/oauth/authorize?client_id=375533386721.377769613264&scope=commands', code=302)

@app.route('/ticket/authorized', methods=['GET', 'POST'])
def tick_calledBack():
    a_code = request.args['code']
    sc = SlackClient("")

    auth_response = sc.api_call(
                                "oauth.access",
                                client_id = os.environ['TICK_CLIENT_ID'],
                                client_secret = os.environ['TICK_CLIENT_SECRET'],
                                code=a_code)

    os.environ["SLACK_USER_TOKEN"] = auth_response['access_token']
    return 'Auth completed.'

@app.route('/surveys/authorize')
def surv_redir():
    return redirect('https://slack.com/oauth/authorize?client_id=375533386721.403631509216&scope=bot')

@app.route('/surveys/authorized', methods=['GET', 'POST'])
def tick_calledBack():
    a_code = request.args['code']
    sc = SlackClient("")

    auth_response = sc.api_call(
                                "oauth.access",
                                client_id = os.environ['SURV_CLIENT_ID'],
                                client_secret = os.environ['SURV_CLIENT_SECRET'],
                                code=a_code)

    os.environ["SURV_USER_TOKEN"] = auth_response['access_token']
    os.environ['SURV_BOT_TOKEN'] = auth_response['bot']['bot_access_token']
    return 'Auth completed.'

if __name__ == '__main__':
    app.run(debug=True,port=5001)
