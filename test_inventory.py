# test_inventory.py

import pytest

from inventory import calculate_restock_order


def test_normal_restock():
    result = calculate_restock_order(
        current_stock=40,
        reorder_point=50,
        max_capacity=100,
        high_velocity=False,
        supplier_batch_size=10,
    )

    assert result == 60


def test_high_velocity_restock():
    result = calculate_restock_order(
        current_stock=40,
        reorder_point=50,
        max_capacity=100,
        high_velocity=True,
        supplier_batch_size=10,
    )

    assert result == 70


def test_negative_stock():
    with pytest.raises(ValueError):
        calculate_restock_order(
            -1,
            50,
            100,
            False,
            10,
        )


def test_zero_batch_size():
    with pytest.raises(ValueError):
        calculate_restock_order(
            10,
            50,
            100,
            False,
            0,
        )


def test_invalid_capacity():
    with pytest.raises(ValueError):
        calculate_restock_order(
            10,
            100,
            100,
            False,
            10,
        )