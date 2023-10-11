from injector import Injector
from injector import singleton

from services.production_issue import ProductionIssue
from services.service import User


def configure(binder):
    binder.bind(
        User,
        to=User(),
        scope=singleton
    )
    binder.bind(
        ProductionIssue,
        to=ProductionIssue(),
        scope=singleton
    )
