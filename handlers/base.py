import aiohttp_jinja2 # v3

from datetime import datetime

from aiohttp import web
from aiohttp_session import get_session

class Index(web.View):
    """ Главная страница """

    @aiohttp_jinja2.template('index.html') # v3
    async def get(self):
        """ [GET] Главная страница """
        conf = self.app['config']
        return dict(conf=conf)

class Login(web.View):
    """ Страница Вход в аккаунт """

    @aiohttp_jinja2.template('login.html') # v3
    async def get(self):
        """ [GET] Страница Вход в аккаунт \n
        : session : хранит datetime последнего посещения"""
        session = await get_session(self)
        session['last_visit'] = str(datetime.utcnow())
        last_visit = session['last_visit']


        text = f'Last visited: {last_visit}'
        return dict(text=f'login Aiohttp!, {text}')

    async def post(self):
        """ [POST] Страница Вход в аккаунт """
        data = await self.post()
        login = data['login']
        password = data['password']

        session = await get_session(self)
        session['user'] = {'login': login}

        location = self.app.router['index'].url_for()
        return web.HTTPFound(location)

class Signup(web.View):
    """ Страница Регистрация """
    async def get(self):
        """ [GET] Страница Регистрация """

        return web.Response(text = 'signup Aiohttp!')