import os
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from modules.gpt import gpt_chat

# read .env
load_dotenv( )
slack_app_token = os.environ['SLACK_APP_TOKEN']
slack_bot_token = os.environ['SLACK_BOT_TOKEN']

# instance
app = App(token=slack_bot_token)

# listener
@app.message("")
def message_hello(message: dict, say):
    res = gpt_chat(message['text'])
    print(res)
    say(res)


#  main
if __name__ == "__main__":
    SocketModeHandler(app,  slack_app_token).start()
