from elemental_server import Server


def test_server_instantiation():
    server = Server()

    assert isinstance(server, Server)
