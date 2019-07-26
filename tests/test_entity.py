from ddd_base.entity import Entity


def test_entity_sets_ids():
    an_entity = Entity()

    assert an_entity.id is not None
