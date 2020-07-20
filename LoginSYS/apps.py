from django.apps import AppConfig


class LoginsysConfig(AppConfig):
    name = 'LoginSYS'

    def ready(self) :
        import LoginSYS.signals
