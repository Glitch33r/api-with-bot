from automate.bot import AutomatedBot
from rest_framework.response import Response
from rest_framework import status

bot = AutomatedBot("F:/api_with_bot/automate/config.yaml", 'http://127.0.0.1:8081/api/sn/')
bot.get_config()
bot.signup()
bot.create_post()
bot.like_posts()


# def automate_api(request, type):
#     if type == 'config':
#         bot.get_config()
#     elif type == 'sign-up':
#         s = bot.signup()
#     elif type == 'post':
#         s = bot.create_post()
#     elif type == 'like':
#         s = bot.like_posts()
#
#     return Response(s, status=status.HTTP_200_OK)
