import pytest

from sale_path import Traveler, create_example, walk_algo


def test_create_traveler():
    traveler = Traveler()
    print(type(traveler))
    assert isinstance(traveler, Traveler)


@pytest.fixture
def example_graph_1():
    return create_example()


def test_walk_algo(example_graph_1):
    head, node_list = example_graph_1
    walked = walk_algo(head)
    assert len(walked) == len(node_list)
    for node in walked:
        assert node in node_list
    for node in node_list:
        assert node in walked

