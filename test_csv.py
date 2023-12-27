import pytest

def test_calculate_average():
    assert calculate_average(grades_data, 'Test1') == pytest.approx(expected_value, abs=1e-2)