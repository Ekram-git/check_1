# test.py

def test_hello_world():
    assert "Hello, world!" in capture_console_output(main)

def test_values():
    x = 10
    y = 20
    assert f"The value of x is: {x} and the value of y is: {y}" in capture_console_output(main)

def test_formatted_string():
    name = "Alice"
    age = 30
    assert f"My name is {name} and I am {age} years old." in capture_console_output(main)

def test_sum():
    a = 5
    b = 7
    assert f"The sum of {a} and {b} is {a + b}" in capture_console_output(main)
