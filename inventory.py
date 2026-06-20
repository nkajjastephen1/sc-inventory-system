# inventory.py

from math import ceil


def calculate_restock_order(
    current_stock: int,
    reorder_point: int,
    max_capacity: int,
    high_velocity: bool,
    supplier_batch_size: int,
) -> int:
    """
    Calculate supplier order quantity.
    """

    if not isinstance(high_velocity, bool):
        raise TypeError("high_velocity must be a boolean.")

    for value, name in [
        (current_stock, "current_stock"),
        (reorder_point, "reorder_point"),
        (max_capacity, "max_capacity"),
        (supplier_batch_size, "supplier_batch_size"),
    ]:
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer.")

    if current_stock < 0:
        raise ValueError("current_stock cannot be negative.")

    if reorder_point < 0:
        raise ValueError("reorder_point cannot be negative.")

    if max_capacity < 0:
        raise ValueError("max_capacity cannot be negative.")

    if max_capacity <= reorder_point:
        raise ValueError(
            "max_capacity must be greater than reorder_point."
        )

    if supplier_batch_size <= 0:
        raise ValueError(
            "supplier_batch_size must be greater than zero."
        )

    if current_stock >= reorder_point:
        return 0

    order_quantity = max_capacity - current_stock

    if high_velocity:
        safety_stock = ceil(order_quantity * 0.15)
        order_quantity += safety_stock

    order_quantity = (
        ceil(order_quantity / supplier_batch_size)
        * supplier_batch_size
    )

    return order_quantity