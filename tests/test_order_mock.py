from unittest.mock import Mock

# 简化的订单查询函数
def answer_order_status(order_id, query_order):
    try:
        order = query_order(order_id)
    except TimeoutError:
        return "订单查询超时，暂时无法确定状态"

    return f"订单状态：{order['status']}"
# 用mock模拟查询成功
def test_answer_order_status_success():
    query_order = Mock(return_value={"status":"已发货"})
    result = answer_order_status("A100", query_order)
    assert result == "订单状态：已发货"
    query_order.assert_called_once_with("A100")


# 用mock模拟订单超时
def test_answer_order_status_failure():
    query_order = Mock(side_effect=TimeoutError("查询超时"))
    result = answer_order_status("A100", query_order)
    assert result == "订单查询超时，暂时无法确定状态"
    query_order.assert_called_once_with("A100")