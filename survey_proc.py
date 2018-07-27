import os
from dotenv import load_dotenv
from slackclient import SlackClient
from textwrap import dedent
from slack_parse import parse


# initialize dotenv
dotenv_path = os.path.join(os.path.dirname(__file__),'.env')
load_dotenv(dotenv_path)

def parse_input(json):
    """Turns an email into a slack-friendly message.

    Takes an email in the form of a JSON POST and formats it into a
    message appropriate to be posted into a Slack channel.

    Args:
        json: A dictionary containing keys 'subject' and 'body'.

    Returns:
        A string that has been formatted to fit with slack standards.
    """
    # isolates and links ticket for internal use.
    tick_link = parse(json['subject'][6:])[0]
    # isolates the ticket title.
    title = " ".join(json['subject'].split()[1:])
    # Indexes rows of the email body.
    bod_list = json['body'].split("\n")
    # Isolates user and survey comments without hardcoding lines.
    for line in bod_list:
        if line.startswith("Requester: "):
            user = line[11:]
        elif line.startswith("Survey Comments"):
            first_q = line.rindex('"',0,-2)
            comments = line[first_q+1:-2]
    # Format slack post
    post = dedent('''\
    Good news, everyone! Another happy customer:\n
    *{0}* had good feedback about ticket {1}: *{2}*\n
    _{3}_\n
    Well done!
    '''.format(user, tick_link, title, comments))
    return post

def post_survey(json):
    """ Takes a JSON object and posts it to a slack channel.

    Calls parse_input function to format the JSON into a string, then
    uses the slack API to

    Args:
        json: A dictionary containing keys 'subject' and 'body'.
    """
    post = parse_input(json)
    sc = SlackClient(os.environ['SURV_BOT_TOKEN'])
    sc.api_call(
                "chat.postMessage",
                channel ='CB22B55EW',
                text = post)

def main():
    test_json = {
        "subject":"[TICK:90000] Hello, World!",
        "body":'This is a body.\nSurvey Comments:"Only this should be isolated".\nRequester: Me'}
    post_survey(test_json)


if __name__ == '__main__':
    main()
