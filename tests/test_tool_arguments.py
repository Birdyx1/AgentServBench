import pytest


def is_valid_query_arguments(arguments: dict) -> bool:
    # 在这里编写校验逻辑
    ...
    order_id = arguments.get("order_id",None)
    if order_id is None:
        return False
    elif order_id == "":
        return False
    elif not isinstance(order_id, str):
        return False
    return True


@pytest.mark.parametrize(
    "arguments,expected",
    [
        ({"order_id": "A100"},True),
        ({"order_id": 100},False),
        ({},False),
        ({"order_id": ""},False)
    ]
)
def test_is_valid_refund_arguments(arguments,expected) -> bool:
    # 在这里编写校验逻辑
    assert is_valid_query_arguments(arguments) == expected
