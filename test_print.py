# test.py
import subprocess

def test_hello_world():
    assert "Hello, world!" in run_script_and_capture_output("print('Hello, world!')")

def test_values():
    x = 10
    y = 20
    expected_output = f"The value of x is: {x} and the value of y is: {y}"
    assert expected_output in run_script_and_capture_output(f"print('The value of x is:', {x}, 'and the value of y is:', {y})")

def test_formatted_string():
    name = "Alice"
    age = 30
    expected_output = f"My name is {name} and I am {age} years old."
    assert expected_output in run_script_and_capture_output(f"print(f'My name is {name} and I am {age} years old.')")

def test_sum():
    a = 5
    b = 7
    expected_output = f"The sum of {a} and {b} is {a + b}"
    assert expected_output in run_script_and_capture_output(f"print('The sum of {a} and {b} is {a + b}')")

def run_script_and_capture_output(script):
    return subprocess.check_output(['python', '-c', script], text=True)
