# Sample Input 1:
#
# 8 11
# Sample Output 1:
#
# expected 8, got 11
# Sample Input 2:
#
# 11 11
# Sample Output 2:
#
# Sample Input 3:
#
# 11 15
# Sample Output 3:
#
# expected 11, got 15


def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result, f"expected {expected_result}, got {actual_result}"

test_input_text(11, 11)
test_input_text(8,11)



