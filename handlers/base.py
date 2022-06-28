from datetime import datetime

from aiohttp import web
from aiohttp_session import get_session

class Index(web.View):
    """ Главная страница """
    async def get(self):
        """ [GET] Главная страница """
        conf = self.app['config']
        return web.Response(text = 'Hello Aiohttp!')

class Login(web.View):
    """ Страница Вход в аккаунт """
    async def get(self):
        """ [GET] Страница Вход в аккаунт \n
        : session : хранит datetime последнего посещения"""
        session = await get_session(self)
        session['last_visit'] = str(datetime.utcnow())
        last_visit = session['last_visit']
        text = f'Last visited: {last_visit}'
        return web.Response(text = f'login Aiohttp!, {text}')

    async def post(self):
        """ [POST] Страница Вход в аккаунт """
        return web.Response(text = 'login Aiohttp!')

class Signup(web.View):
    """ Страница Регистрация """
    async def get(self):
        """ [GET] Страница Регистрация """

        return web.Response(text = 'signup Aiohttp!')