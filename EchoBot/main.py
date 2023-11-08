from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import os
from dotenv import load_dotenv

# read .env
load_dotenv()
slack_app_token = os.environ['SLACK_APP_TOKEN']
slack_bot_token = os.environ['SLACK_BOT_TOKEN']

# instance
app = App(token=slack_bot_token)

# listener
@app.message("")
def message_hello(message, say):
    user_name = message['user']
    say(f"<@{user_name}>さんは以下のメッセージを送信しました\n{message['text']}")
    # say(f"Hey there <@{message['user']}>!")
    # print(message['text'])
    # print(message.keys())


#  main
if __name__ == "__main__":
    SocketModeHandler(app,  slack_app_token).start()
