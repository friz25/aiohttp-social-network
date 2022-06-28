from aiohttp import web

async def index(request):
    """ Главная страница """
    conf = request.app['config']
    return web.Response(text = 'Hello Aiohttp!')

async def login(request):
    """ Страница Вход в аккаунт """
    return web.Response(text = 'login Aiohttp!')

async def signup(request):
    """ Страница Регистрация """
    return web.Response(text = 'signup Aiohttp!')