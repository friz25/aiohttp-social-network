import aiohttp_jinja2 # v3

from datetime import datetime

from aiohttp import web
from aiohttp_session import get_session

from models.user import User # v4

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

        """ v4 """
        db = self.app['db']
        user = await User.get_user(db=db)
        document = await db.test.find_one()

        return dict(last_visit=f'login Aiohttp!, Last visited: {last_visit}')

    async def post(self):
        """ [POST] Страница Вход в аккаунт """
        data = await self.post()
        login = data['login']
        password = data['password']

        session = await get_session(self)
        session['user'] = {'login': login}

        location = self.app.router['index'].url_for()
        return web.HTTPFound(location=location)

class Signup(web.View):
    """ Страница Регистрация """
    async def get(self):
        """ [GET] Страница Регистрация """

        return web.Response(text='signup Aiohttp!')