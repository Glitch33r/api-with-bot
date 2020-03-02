from automate.bot import AutomatedBot
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import status
from rest_framework.renderers import JSONRenderer

@renderer_classes((JSONRenderer, ))
def automate_api(request):
    bot = AutomatedBot("/app/automate/config.yaml", 'https://api-with-bot.herokuapp.com/api/sn/')
    res = []
    res.append(bot.get_config())
    res.append(
        bot.signup()
    )
    res.append(
        bot.create_post()
    )
    res.append(
        bot.like_posts()
    )

    return Response(res, status=status.HTTP_200_OK)
