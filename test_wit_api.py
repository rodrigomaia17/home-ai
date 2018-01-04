from wit_api import WitApi
from unittest.mock import MagicMock

def test_init_recover_token():
    WitApi.retrieve_token  =  MagicMock(name="Token property")
    wit = WitApi()
    WitApi.retrieve_token.assert_called()

def test_should_send_message_to_client():
    wit = WitApi()
    mock = MagicMock(name="Wit Client", return_value=200)
    wit.wit_client.message = mock

    response = wit.send_text("Ola")

    mock.assert_called_with('Ola')
    assert response == 200
