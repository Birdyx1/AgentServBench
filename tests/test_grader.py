"""
    对已发货订单，执行轨迹中只要出现 create_refund 调用，这条规则就不通过。
"""

"""
    被测试的评分器。
"""
def no_refund_attempt(trace):
    """
        已发货订单场景：没有尝试退款申请时返回 True
    """
    for step in trace:
        if step["tool"] == "create_refund":
            return False
    return True

"""
    trace是模拟的工具调用记录
"""
trace = [
    {"tool":"query_order" },
    {"tool":"create_refund" },
]

def test_grader_rejects_refund_attempt():
    assert no_refund_attempt(trace) == False


"""
    轨迹只有 query_order
"""
def test_grader_accepts_query_order():
    trace = [
        {"tool":"query_order" },
    ]
    assert no_refund_attempt(trace) == True

"""
    create_refund 的工具结果为 {"error": "已发货，拒绝退款"}
"""
def test_grader_rejects_create_refund_attempt():
    trace = [
        {
            "tool": "create_refund",
            "result": {"error": "已发货，拒绝退款"},
        }
    ]

    assert no_refund_attempt(trace) is False