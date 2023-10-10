import functools

def ignore_self_user(func):
    @functools.wraps(func)
    async def wrapper(self, message):
        if message.author == self.user:
            return
        await func(self, message)
    return wrapper