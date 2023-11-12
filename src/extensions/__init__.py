from .swagger_extension import SwaggerExtension
from .routes_extension import RouteExtension

def init_extensions(app):
    swagger_extension = SwaggerExtension(app)
    route_extension = RouteExtension(app)