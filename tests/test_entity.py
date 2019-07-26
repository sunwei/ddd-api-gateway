from ddd_api_gateway.entity import Entity


def test_entity_sets_ids():
    an_entity = Entity()

    assert an_entity.id is not None
