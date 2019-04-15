import falcon

from resources.trackers import CartTrackerResource
from resources.settings import PATH
from tests.utils import make_item


def fake_async_write(self, cart_id, payload):
    pass


def test_cookie_mechanism(
    monkeypatch, api_test_client
):
    monkeypatch.setattr(CartTrackerResource, "async_write", fake_async_write)

    result = api_test_client.simulate_post(
        PATH,
        json=make_item()
    )
    cookies = result.cookies
    assert 'cart_id' in cookies
    assert result.status == falcon.HTTP_204

    result = api_test_client.simulate_post(
        PATH,
        json=make_item()
    )
    assert not (
        cookies.get('cart_id').value == result.cookies.get('cart_id').value
    )
    assert result.status == falcon.HTTP_204

    result = api_test_client.simulate_post(
        PATH,
        json=make_item(),
        headers={'Cookie': f"cart_id={cookies.get('cart_id').value}"}
    )
    assert 'cart_id' not in result.cookies
    assert result.status == falcon.HTTP_204
