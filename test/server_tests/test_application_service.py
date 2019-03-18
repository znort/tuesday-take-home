import pytest
from aiohttp import web

from services.application.application_service import ApplicationService
from services.domain.greeter_service import GreeterService


@pytest.fixture
def client(loop, aiohttp_client):
    app = web.Application()
    greeter_service = GreeterService()

    mock_service = ApplicationService(app.router, greeter_service)
    app['application_service'] = mock_service
    return loop.run_until_complete(aiohttp_client(app))


async def test_greeting(client):
    resp = await client.get('/')
    assert resp.status == 200
    text = await resp.text()
    assert 'Hello, world' in text
