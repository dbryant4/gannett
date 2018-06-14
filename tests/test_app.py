def test_invalid_endpoint(client):
    """ Test that an undefined endpoint returns 404 """

    result = client.get('/nonsense')
    assert result.status_code == 404

def test_invalid_parameter(client):
    """ Test that an undefined parameter returns 404 """

    result = client.get('/?unknownparam')
    assert result.status_code == 404
