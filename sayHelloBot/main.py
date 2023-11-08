from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os
from dotenv import load_dotenv

# .envファイルを読み込む
load_dotenv()

slack_api_token = os.getenv('SLACK_BOT_API_KEY')


def SendToSlackMessage(message):
    client = WebClient(token=slack_api_token)
    response = client.chat_postMessage(channel='C063WEJ9WR5', text=message)


SendToSlackMessage("Helloworld!")
