import base64 # v2
import logging
import aiohttp_jinja2 # v3
import jinja2 # v3
from aiohttp import web

from cryptography import fernet # v2
from aiohttp_session import setup # v2
from aiohttp_session.cookie_storage import EncryptedCookieStorage # v2

from routes.base import setup_routes
from config.common import BaseConfig

def main():
    app = web.Application()

    """ Генерируем ключ aiohttp-сессии \n
    теперь у каждого пользователя (зашедшего на сайт) будет храниться свой coockie-ключ - идентификатор"""
    fernet_key = fernet.Fernet.generate_key() # v2
    secret_key = base64.urlsafe_b64decode(fernet_key) # v2
    setup(app, EncryptedCookieStorage(secret_key)) # v2

    aiohttp_jinja2.setup(app, loader=jinja2.PackageLoader(package_name="main", package_path="templates"))

    setup_routes(app)
    app['config'] = BaseConfig
    logging.basicConfig(level=logging.DEBUG)
    web.run_app(app)

if __name__ == '__main__':
    main()