def test_root_no_parameters(client):
    """ Test GET / returns "hello world" """

    result = client.get('/')
    assert result.data == 'hello world'
    assert result.status_code == 200


def test_root_with_uppercase(client):
    """ Test GET /?uppercase returns "HELLO WORLD" """

    result = client.get('/?uppercase')
    assert result.data == 'HELLO WORLD'
    assert result.status_code == 200


def test_root_with_reversed(client):
    """ Test GET /?reversed returns "dlrow olleh" """

    result = client.get('/?reversed')
    assert result.data == 'dlrow olleh'
    assert result.status_code == 200


def test_root_with_reversed_and_uppercase(client):
    """ Test GET /?reversed&uppercase returns "DLROW OLLEH" """

    result = client.get('/?reversed&uppercase')
    assert result.data == 'DLROW OLLEH'
    assert result.status_code == 200
