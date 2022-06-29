class User:

    collection = None

    def __init__(self):
        pass
    '''
    @classmethod
    async def get_user(cls, uid):
        return cls.collection.find_one(uid)
    '''
    @classmethod
    async def get_user(db, uid):
        return await db.users.find_one(uid)