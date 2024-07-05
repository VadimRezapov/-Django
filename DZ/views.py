import logging

from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    response = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Город Санкт-Петербург</title>
    </head>
    <body>
    <h1>Город Санкт-Петербург</h1>
    <p>Санкт-Петербург - крупнейший культурный и исторический центр России. Город был основан в 1703 году Петром I и является одним из самых красивых городов мира.</p>
    <p>И в этом городе живу я - Станислав, студент GeekBrains.</p>
    """
    logger.info("index page was requested")

    return HttpResponse(response)


def about(request):
    response = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Обо мне</title>
    </head>
    <body>
    <h1>Привет, меня зовут Станислав!</h1>
    <p>Я живу в красивом городе Санкт-Петербурге и обучаюсь на программе "Разработчик Python" в GeekBrains. Я увлечен программированием и надеюсь успешно закончить курс, чтобы начать новую карьеру в IT сфере.</p>
    <p>Я верю, что с усердием, настойчивостью и любовью к изучению новых технологий я смогу добиться успеха и найти работу по новой специальности. У меня есть цель и я готов учиться и развиваться, чтобы достичь ее.</p>
    <p>Желаю себе удачи в этом увлекательном пути и верю, что все у меня получится! =)</p>
    <p>Пожелайте мне удачи!</p>
    </body>
    </html>
    """
    logger.info("about page was requested")

    return HttpResponse(response)