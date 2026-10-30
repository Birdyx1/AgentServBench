import pytest

@pytest.fixture
def paid_order():
    return {
        "order_id": "A100",
        "is_paid": True,
        "is_shipped": False,
    }


def test_shipped_order_has_no_refund():
    refund_count = 0
    assert refund_count == 0

def can_request_refund(is_paid, is_shipped):
    return is_paid and not is_shipped



@pytest.mark.parametrize(
    "is_paid, is_shipped, expected",
    [
        (True, False, True),   # 已支付、未发货
        (True, True, False),   # 已支付、已发货
        (False,False,False),   # 未支付、未发货
        (False,True,False),    # 未支付、已发货
    ],
)
def test_refund_eligibility(is_paid, is_shipped, expected):
    assert can_request_refund(is_paid, is_shipped) is expected

@pytest.mark.parametrize(
    "is_shipped, expected",
    [
        (True, True),
        (False, False),
    ],
)
def test_order_can_be_marked_shipped(paid_order,is_shipped, expected):
    paid_order["is_shipped"] = is_shipped

    assert paid_order["is_shipped"] is expected

def test_paid_order_initial_state(paid_order):
    assert paid_order["is_shipped"] is False