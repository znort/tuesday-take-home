from aiohttp import web

from services.application.abstract_application_service import AbstractApplicationService


class ApplicationService(AbstractApplicationService):

    def __init__(self, router, greeter_service=None, base_path=""):
        self.greeter_service = greeter_service
        self.base_path = base_path
        super().__init__(router)

    async def say_hello(self, request):
        greeting = await self.greeter_service.say_hello()
        return web.Response(text=greeting)

    def register_routes(self, router):
        router.add_routes([web.get(self.base_path + '/', self.say_hello)])
