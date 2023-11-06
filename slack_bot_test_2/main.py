from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import os
from dotenv import load_dotenv

# .envファイルを読み込む
load_dotenv()

slack_app_token = os.environ['SLACK_APP_TOKEN']
slack_bot_token = os.environ['SLACK_BOT_TOKEN']

app = App(token=slack_bot_token)

# 'hello' を含むメッセージをリッスンします
# 指定可能なリスナーのメソッド引数の一覧は以下のモジュールドキュメントを参考にしてください：
# https://slack.dev/bolt-python/api-docs/slack_bolt/kwargs_injection/args.html


@app.message("")
def message_hello(message, say):
    # イベントがトリガーされたチャンネルへ say() でメッセージを送信します
    say(f"Hey there <@{message['user']}>!")
    # print(message['text'])
    print(message.keys())


# アプリを起動します
if __name__ == "__main__":
    SocketModeHandler(app,  slack_app_token).start()
