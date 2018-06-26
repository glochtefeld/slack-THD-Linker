import os
import re

from flask import abort, Flask, jsonify, request


app = Flask(__name__)


def is_request_valid(request):
    is_token_valid = request.form['token'] == os.environ['VERIFICATION_TOKEN']
    is_team_id_valid = request.form['team_id'] == os.environ['TEAM_ID']

    return is_token_valid and is_team_id_valid

def parse(txt):
    txt = txt.split()
    buildStr = ""
    for word in txt:
        if re.search(".*\d{5,7}",tryStr):
            buildStr = "<https://helpdesk.luther.edu/adminui/ticket.php?ID=" + word + '>'
            return buildStr
        else:
            buildStr = "No ticket found."

@app.route('/ticket', methods=['POST'])
def hello_there():
    if not is_request_valid(request):
        abort(400)
    text = request.form.get('text',None)
    resText = parse(text)

    return jsonify({'response_type':'in_channel','text':resText})

if __name__ == '__main__':
    app.run(debug=True,port=5001)
