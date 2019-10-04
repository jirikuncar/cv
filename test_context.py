import context


def test_empty_context():

    class Empty(context.Node):
        pass

    assert '@context' in Empty
