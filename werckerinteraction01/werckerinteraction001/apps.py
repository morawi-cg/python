from django.apps import AppConfig
import ConnectToWercker

class Werckerinteraction001Config(AppConfig):
    name = 'werckerinteraction001'
    ConnectToWercker()

