from chapter08.src.case08.case08 import acquire_data


def test_acquire_data_with_valid_data():
    # given
    input_data = """city,country,phone
Bangalore,India,+91-80-12345678
New York,USA,+1-212-12345678
Delhi,India,+91-11-98765432
London,UK,+44-20-12345678"""

    # when
    result = acquire_data(input_data)

    # then
    assert len(result) == 2
    assert result[0] == {"city": "Bangalore", "phone": "+91-80-12345678"}
    assert result[1] == {"city": "Delhi", "phone": "+91-11-98765432"}


def test_acquire_data_with_empty_lines():
    # given
    input_data = """city,country,phone
Bangalore,India,+91-80-12345678

Delhi,India,+91-11-98765432
"""

    # when
    result = acquire_data(input_data)

    # then
    assert len(result) == 2
    assert result[0] == {"city": "Bangalore", "phone": "+91-80-12345678"}
    assert result[1] == {"city": "Delhi", "phone": "+91-11-98765432"}


def test_acquire_data_with_no_india_cities():
    # given
    input_data = """city,country,phone
New York,USA,+1-212-12345678
London,UK,+44-20-12345678"""

    # when
    result = acquire_data(input_data)

    # then
    assert len(result) == 0


def test_acquire_data_with_empty_input():
    # given
    input_data = ""

    # when
    result = acquire_data(input_data)

    # then
    assert len(result) == 0
