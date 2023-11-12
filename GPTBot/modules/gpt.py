import os
from openai import OpenAI
from dotenv import load_dotenv

# read .env
load_dotenv("../.env")
open_ai_org = os.environ['OPENAI_ORGANIZATION']
TOKENS = int(os.environ['TOKEN'])
N = int(os.environ['N'])
STOP: str | None = os.environ['STOP']
TEMPERATURE = float(os.environ['TEMPERATURE'])
TOP_P = float(os.environ['TOP_P'])

# instance
client = OpenAI(
    organization=open_ai_org,)

# gpt_chat() takes a string as input and returns a string as output
def gpt_chat(message: str) -> str:
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",  # model ID
        prompt=message,
        max_tokens=TOKENS,  # 生成するトークンの最大数
        n=N,  # 生成するレスポンスの数
        stop=STOP,  # 停止トークンの設定
        temperature=TEMPERATURE,  # 生成時のランダム性の制御
        top_p=TOP_P,  # トークン選択時の確率閾値
    )
    return response.choices[0].text


# test
if __name__ == "__main__":
    print(gpt_chat("Hello, I'm GPT. I'm a bot."))
