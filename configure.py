from injector import Injector
from injector import singleton
from services.buildtime import BuildTime
from services.production_issue import ProductionIssue
from services.release_defect import ReleaseDefects
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
    binder.bind(
        BuildTime,
        to=BuildTime(),
        scope=singleton
    )
    binder.bind(
        ReleaseDefects,
        to=ReleaseDefects(),
        scope=singleton
    )