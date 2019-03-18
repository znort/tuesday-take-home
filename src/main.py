from aiohttp import web
from aiohttp_swagger import setup_swagger

from services.application.application_service import ApplicationService
from services.domain.greeter_service import GreeterService

BASE_PATH = ''
greeter_service = GreeterService()
app = web.Application()
app_service = ApplicationService(app.router, greeter_service)

setup_swagger(app, swagger_from_file="swagger.yaml", description="Customers-service",
              api_version="1.0.0",
              swagger_url=BASE_PATH + "/swagger")

if __name__ == '__main__':
    # run app locally
    web.run_app(app, port=8080)
