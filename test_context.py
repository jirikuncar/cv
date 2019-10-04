import context


def test_empty_context():

    class Empty(context.Node):
        pass

    assert '@context' in Empty


def test_type():

    PROV = context.NS('http://www.w3.org/ns/prov#')

    class Activity(PROV):
        pass

    assert Activity['@type'] == PROV['@type'] + 'Activity'


def test_field():

    FOAF = context.NS('http://xmlns.com/foaf/0.1/')

    class Field(context.Node):
        field: FOAF / 'name' = 'Fieldname'

    assert Field['@context']['field'] == 'http://xmlns.com/foaf/0.1/name'
    assert Field.field == 'Fieldname'


def test_field_with_pure_namespace_type():

    FOAF = context.NS('http://xmlns.com/foaf/0.1/')

    class Field(context.Node):
        name: FOAF = 'Fieldname'

    assert Field['@context']['name'] == 'http://xmlns.com/foaf/0.1/name'
    assert Field.name == 'Fieldname'

