from project.config.swagger import swagger_config, template
from flasgger import Swagger


class SwaggerExtension:
    def __init__(self, app=None, **kwargs):
        if app is not None:
            self.init_app(app, **kwargs)

    def init_app(self, app: object) -> object:
        Swagger(app, config=swagger_config, template=template)