import pytest

from services.deex_websocket_client import DeexWebsocketClient
import config

@pytest.fixture
def deex_client():
    return DeexWebsocketClient(config.WEBSOCKET_URL)

def test_ws_request(deex_client):
    response = deex_client.request('database', "get_dynamic_global_properties", [])
    assert response['id'] == '2.1.0'
    assert 'head_block_number' in response

def test_automatic_api_id_retrieval(deex_client):
    deex_client.request('asset', 'get_asset_holders', ['1.3.0', 0, 100])

def test_get_object(deex_client):
    object = deex_client.get_object('1.3.0')
    assert object