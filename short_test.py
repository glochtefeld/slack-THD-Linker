import os
from slackclient import SlackClient
from dotenv import load_dotenv

# initialize dotenv
dotenv_path = os.path.join(os.path.dirname(__file__),'.env')
load_dotenv(dotenv_path)

sc = SlackClient(os.environ['SURV_BOT_TOKEN'])
users = sc.api_call("users.list")
for user in users['members']:
    print(user["name"])
