from project.extensions.swagger_extension import SwaggerExtension
from project.extensions.routes_extension import RouteExtension

def init_extensions(app):
    swagger_extension = SwaggerExtension(app)
    route_extension = RouteExtension(app)