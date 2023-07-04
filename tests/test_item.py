import pytest

from src.item import Item


@pytest.fixture
def create_item():
    return Item('TV', 20000, 5)


def test_item_calculate_total_price(create_item):
    assert create_item.calculate_total_price() == 100000


def test_item_apply_discount(create_item):
    Item.pay_rate = 0.5
    create_item.apply_discount()
    assert create_item.price == 10000


def test_item_all_count():
    assert len(Item.all) == 2
