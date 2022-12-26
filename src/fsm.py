from importlib.resources import contents
import os
import re
from socket import MsgFlag
from tkinter.tix import Tree
from transitions.extensions import GraphMachine
from utils import push_flex_message, push_message, send_button_template, send_flex_message, send_text_message, send_image_url

#  載入環境變數
from dotenv import load_dotenv
load_dotenv()

ngrok_url = os.getenv('NGROK_URL' ,None)

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_lobby(self, event):
        return True
    
    def is_going_to_product(self, event):
        text = event.message.text
        return text.lower() == "products"
    
    def is_going_to_aggresive(self, event): #this is not overload
        text = event.message.text
        return text.lower() == "1"

    def is_going_to_figure(self, event): 
        text = event.message.text
        return text.lower() == "2"

    def is_going_to_road(self, event): 
        text = event.message.text
        return text.lower() == "3"

    def is_going_back_lobby(self, event): 
        text = event.message.text
        return text.lower() == "home"
    
    def is_going_to_skill(self, event):
        text = event.message.text
        return text.lower() == "skills"
    
    def is_going_to_brake(self, event):
        text = event.message.text
        return text.lower() == "1"
    
    def is_going_to_grind(self, event):
        text = event.message.text
        return text.lower() == "2"
    # this is initial state
    def on_enter_lobby(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "Welcome to this app!!!\nPlease choose the field you want to know first! (press the button below)")

    def on_enter_product(self, event): #is this overload? that is, on_enter_state?
        reply_token = event.reply_token
        send_text_message(reply_token, "Please choose the field you want to know:\n1) aggresive inline skating\n2) Freestyle slalom skating\n3) Urban skate\nPlease enter the field number, ex: 1")
        #self.go_back()

    def on_enter_skill(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "Please choose the skills you want to know:\n1) grind\n2) brake\nPlease enter the field number, ex: 1")

    def on_enter_aggresive(self, event):
        reply_token = event.reply_token
        url='https://www.inlinewarehouse.com/USD_Sway_Team_IV/descpage-710173.html'
        theme='https://i.im.ge/2022/12/25/q3Uow6.usd-sway-four.png'
        name='USD Sway Team IV'
        description='price: 229 USD\nSkill Level: Beginner and Better'
        send_button_template(reply_token, url, theme, name, description)

        # # this area is send text and img respectively

        # id = event.source.user_id
        # local = ngrok_url + '/static/usd_sway_four.png' 
        # send_image_url(id, local)
        # msg = "USD Sway 4\nprice: ~6000TWD"
        # reply_token = event.reply_token
        # send_text_message(reply_token, msg)

        # use flex_message here, why this cause error?????????????
#         reply_token = event.reply_token
#         content = {
#   "type": "bubble",
#   "hero": {
#     "type": "image",
#     "size": "full",
#     "aspectRatio": "20:13",
#     "aspectMode": "cover",
#     "action": {
#       "type": "uri",
#       "uri": "https://linecorp.com"
#     },
#     "url": "https://i.im.ge/2022/12/25/q3Uow6.usd-sway-four.png"
#   },
#   "body": {
#     "type": "box",
#     "layout": "vertical",
#     "spacing": "md",
#     "action": {
#       "type": "uri",
#       "uri": "https://linecorp.com"
#     },
#     "contents": [
#       {
#         "type": "text",
#         "text": "USD Sway 4",
#         "size": "xl",
#         "weight": "bold"
#       },
#       {
#         "type": "box",
#         "layout": "vertical",
#         "spacing": "sm",
#         "contents": [
#           {
#             "type": "box",
#             "layout": "baseline",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "$199",
#                 "weight": "bold",
#                 "margin": "sm",
#                 "flex": 0
#               },
#               {
#                 "type": "text",
#                 "text": "dollars",
#                 "size": "sm",
#                 "align": "end",
#                 "color": "#aaaaaa"
#               }
#             ]
#           }
#         ]
#       },
#       {
#         "type": "text",
#         "text": "Model Year 2020",
#         "wrap": True,
#         "color": "#aaaaaa",
#         "size": "xxs"
#       },
#       {
#         "type": "text",
#         "text": "Skate Type Aggressive",
#         "wrap": True,
#         "color": "#aaaaaa",
#         "size": "xxs"
#       },
#       {
#         "type": "text",
#         "text": "Skill Level  Beginner and Better",
#         "wrap": True,
#         "color": "#aaaaaa",
#         "size": "xxs"
#       },
#       {
#         "type": "text",
#         "text": "Weight\t1740g (US 8.0 EU 41)",
#         "wrap": True,
#         "color": "#aaaaaa",
#         "size": "xxs"
#       }
#     ]
#   },
#   "footer": {
#     "type": "box",
#     "layout": "vertical",
#     "contents": [
#       {
#         "type": "button",
#         "style": "primary",
#         "color": "#905c44",
#         "margin": "xxl",
#         "action": {
#           "type": "uri",
#           "label": "View more",
#           "uri": "https://www.inlinewarehouse.com/USD_Sway_Team_IV/descpage-710173.html"
#         }
#       }
#     ]
#   }
# }
#         send_flex_message(reply_token, content)

    def on_enter_figure(self, event):
        reply_token = event.reply_token
        url='https://www.locoskates.com/products/seba-e3-80-premium-skates?variant=32937514172459'
        theme='https://i.im.ge/2022/12/25/q3UrXK.e-three.png'
        name='Seba E3 80'
        description='price: 149 USD\nSkill Level: Beginner and Better'
        send_button_template(reply_token, url, theme, name, description)
    
    def on_enter_road(self ,event):
        reply_token = event.reply_token
        url='https://www.inlinewarehouse.com/FR_Skates_FR1_310/descpage-1310B18.html'
        theme='https://i.im.ge/2022/12/25/q3UXKF.fr1.png'
        name='FR1 310'
        description='price: 279 USD\nSkill Level: Intermediate and Better'
        send_button_template(reply_token, url, theme, name, description)
    
    def on_enter_brake(self ,event):
        reply_token = event.reply_token
        url='https://www.wikihow.com/Stop-on-Inline-Skates'
        theme='https://i.im.ge/2022/12/25/q3Elq0.t-stop.png'
        name='T-stop'
        description='fast way to stop'
        send_button_template(reply_token, url, theme, name, description)
    
    def on_enter_grind(self ,event):
        reply_token = event.reply_token
        url='https://riders.co/en/aggressive/grinds'
        theme='https://i.im.ge/2022/12/25/q3EQLm.soul-1.png'
        name='Soul'
        description=' '
        send_button_template(reply_token, url, theme, name, description)
    # def state0_going_to_state2(self, event):
    #     text = event.message.text
    #     return text.lower() == "2"

