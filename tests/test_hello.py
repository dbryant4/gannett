def test_hello_with_reversed(client):
    """ Test GET /hello?reversed returns "olleh" """

    result = client.get('/hello?reversed')
    assert result.data == 'olleh'
    assert result.status_code == 200


def test_hello_with_uppercase(client):
    """ Test GET /hello?uppercase returns "HELLO" """

    result = client.get('/hello?uppercase')
    assert result.data == 'HELLO'
    assert result.status_code == 200


def test_hello_with_reversed_uppercase(client):
    """ Test GET /hello?reversed&uppercase returns "OLLEH" """

    result = client.get('/hello?reversed&uppercase')
    assert result.data == 'OLLEH'
    assert result.status_code == 200


def test_hello_with_reversed_uppercase(client):
    """ Test GET /hello?reversed&uppercase returns "OLLEH" """

    result = client.get('/hello?reversed&uppercase')
    assert result.data == 'OLLEH'
    assert result.status_code == 200
