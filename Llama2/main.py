import os
from dotenv import load_dotenv
from typing import Final
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from modules.Llama import Llama_chat

# read .env
load_dotenv()
slack_app_token = os.environ['SLACK_APP_TOKEN']
slack_bot_token = os.environ['SLACK_BOT_TOKEN']

# instance
app = App(token=slack_bot_token)

# listener
@app.message("")
def chat(message: dict, say):
    output: Final[str] = Llama_chat(message['text'])
    print(output)
    say(output)


#  main
if __name__ == "__main__":
    SocketModeHandler(app,  slack_app_token).start()
