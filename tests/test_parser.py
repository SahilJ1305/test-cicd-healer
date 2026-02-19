from src.parser import parse_data, calculate_mean

def test_parse_data():
    result = parse_data({"col1": [1, 2], "col2": [3, 4]})
    assert result is not None

def test_calculate_mean():
    assert calculate_mean([1, 2, 3, 4, 5]) == 3.0
