
import os
import sys

#載入LineBot所需要的套件
from flask import Flask, request, jsonify, abort, send_file
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, FlexSendMessage 

from machine import create_machine
from utils import send_flex_message, send_text_message

#  載入環境變數
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__, static_url_path="/static/") # this name have to be static

#畫圖用
os.environ["PATH"] += os.pathsep + 'D:/Graphviz/bin/'

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)


# Unique FSM for each user
machines = {}
machine = create_machine()

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi(channel_access_token)
# 必須放上自己的Channel Secret
parser = WebhookParser(channel_secret)

# line_bot_api.push_message('U30b96aadb91f8304ac2fbd12e709cdaf', TextSendMessage(text='hello!!!')) #front is user id in line_dev , this is push
# line_bot_api.reply_message(event.reply_token,TextSendMessage(text='hello!!!')) this is replay


# 監聽所有來自 /callback 的 Post Request
# @app.route("/callback", methods=['POST'])
# def callback():
#     # get X-Line-Signature header value
#     signature = request.headers['X-Line-Signature']

 
#     # get request body as text
#     body = request.get_data(as_text=True)
#     app.logger.info("Request body: " + body)

#     # handle webhook body
#     try:
#         handler.handle(body, signature)
#     except InvalidSignatureError:
#         abort(400)

#     return 'OK'


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")
    
    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)
    
    machine.get_graph().draw("../fsm.png", prog="dot", format="png")
    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        
        
        if event.source.user_id not in machines:
            machines[event.source.user_id] = create_machine()

        response = machines[event.source.user_id].advance(event)
        if response == False:
            send_text_message(event.reply_token, "Please enter the right format")

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    # machine.get_graph().draw("../fsm.png", prog="dot", format="png")
    return send_file("../fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 5000)
    app.run(host="0.0.0.0", port=port) #debug 開啟同步更新
