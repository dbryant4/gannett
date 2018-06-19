def test_world_with_reversed(client):
    """ Test GET /world?reversed returns "dlrow" """

    result = client.get('/world?reversed')
    assert result.data == 'dlrow'
    assert result.status_code == 200


def test_world_with_uppercase(client):
    """ Test GET /world?uppercase returns "WORLD" """

    result = client.get('/world?uppercase')
    assert result.data == 'WORLD'
    assert result.status_code == 200


def test_world_with_reversed_uppercase(client):
    """ Test GET /world?reversed&uppercase returns "DLROW" """

    result = client.get('/world?reversed&uppercase')
    assert result.data == 'DLROW'
    assert result.status_code == 200


def test_world_with_reversed_uppercase(client):
    """ Test GET /world?reversed&uppercase returns "DLROW" """

    result = client.get('/world?reversed&uppercase')
    assert result.data == 'DLROW'
    assert result.status_code == 200
