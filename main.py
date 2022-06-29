import base64 # v2
import logging
import aiohttp_jinja2 # v3
import jinja2 # v3
from aiohttp import web

from cryptography import fernet # v2
from aiohttp_session import setup # v2
from aiohttp_session.cookie_storage import EncryptedCookieStorage # v2
from motor.motor_asyncio import AsyncIOMotorClient # v4

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
    app['db'] = AsyncIOMotorClient().my_database #Подключили Mongo БД

    logging.basicConfig(level=logging.DEBUG)
    web.run_app(app)

if __name__ == '__main__':
    main()
'''Добавляем пользователей в MongoDB через терминал:
mongo my_database
db.users.insertOne({"first_name" : "Anton", "last_name" : "Kozachenko", "email": "kakaka@gmail.com", "password": "fwvt7nnj4qfed09o"})
db.users.insertOne({"first_name" : "Victor", "last_name" : "Dibbet", "email": "kak2131aka@gmail.com", "password": "9rzk8p4k09yo6p0d"})
db.users.insertOne({"first_name" : "Sasha", "last_name" : "Credit", "email": "kaka1111ka@gmail.com", "password": "uc3cqkt9vdjl5l9e"})
db.users.insertOne({"first_name" : "Voldemort", "last_name" : "HolyMoly", "email": "kak4545aka@gmail.com", "password": "1w8l67p6nold9wix"})
db.users.insertOne({"first_name" : "Kesha", "last_name" : "Dzeba", "email": "kakak67676a@gmail.com", "password": "g1lhsmsjsz89voy4"})
'''