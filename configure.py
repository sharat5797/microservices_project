from injector import Injector
from injector import singleton
from services.service import User

def configure(binder):
    binder.bind(
        User,
        to=User(),
        scope=singleton
    )